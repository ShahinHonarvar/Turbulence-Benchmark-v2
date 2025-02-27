def all_left_truncatable_prime(t):
    x = t[803]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    left_truncatable_primes = []
    for n in range(2, x):
        if not any(str(n).endswith('0')):
            if is_prime(n):
                is_left_truncatable = True
                for digit in str(n):
                    n = int(str(n)[1:])
                    if not is_prime(n):
                        is_left_truncatable = False
                        break
                if is_left_truncatable:
                    left_truncatable_primes.append(n)
    return sorted(left_truncatable_primes)