def all_right_truncatable_prime(data):

    def check_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def check_truncatable(n):
        snn = str(n)
        return all((check_prime(int(snn[i:])) for i in range(len(snn) - 1)))
    x = data[52]
    primes = [i for i in range(2, x) if check_prime(i)]
    truncatables = list(filter(check_truncatable, primes))
    return sorted(truncatables, reverse=True)