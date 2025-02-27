def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(x):

    def check_truncatable(n):
        n = str(n)
        for i in range(1, len(n)):
            if is_prime(int(n[i:])) is False:
                return False
        return True
    primes = [i for i in range(2, x) if is_prime(i)]
    left_truncatable_primes = [i for i in primes if check_truncatable(i)]
    return sorted(left_truncatable_primes, reverse=True)