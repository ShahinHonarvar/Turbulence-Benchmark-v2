def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = t[49]
    left_truncatable_primes = []
    for num in range(2, x):
        if '0' not in str(num) and all((is_prime(int(str(num)[i:])) for i in range(1, len(str(num))))):
            left_truncatable_primes.append(num)
    return sorted(left_truncatable_primes)