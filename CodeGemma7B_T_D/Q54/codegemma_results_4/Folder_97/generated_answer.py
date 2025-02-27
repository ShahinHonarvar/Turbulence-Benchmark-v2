def all_right_truncatable_prime(t):
    x = t[645]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    right_truncatable_primes = []
    for num in range(3, x, 2):
        if is_prime(num):
            digit = num % 10
            truncatable = True
            num //= 10
            while num > 0:
                if not is_prime(num):
                    truncatable = False
                    break
                digit = num % 10
                num //= 10
            if truncatable:
                right_truncatable_primes.append(num)
    right_truncatable_primes.sort()
    return right_truncatable_primes