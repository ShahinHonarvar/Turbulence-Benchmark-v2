def all_right_truncatable_prime(integers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    num = integers[39]
    primes = []
    for i in range(num - 1, 0, -1):
        if is_prime(i):
            trunc = i
            while trunc > 1:
                trunc //= 10
                if not is_prime(trunc):
                    break
            else:
                primes.append(i)
    return sorted(primes, reverse=True)