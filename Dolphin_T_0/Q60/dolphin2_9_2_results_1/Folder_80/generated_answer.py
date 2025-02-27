def all_left_right_truncatable_prime(x):

    def is_left_right_truncatable_prime(n):
        if n < 10:
            return is_prime(n)
        elif n % 10 == 0 or n // 10 % 10 == 0:
            return False
        else:
            return is_prime(n) and is_left_right_truncatable_prime(n // 10) and is_left_right_truncatable_prime(n % 10)

    def is_prime(n):
        if n == 1:
            return False
        else:
            for i in range(2, round(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
    left_right_truncatable_primes = []
    for i in range(2, x + 1):
        if is_left_right_truncatable_prime(i):
            left_right_truncatable_primes.append(i)
    left_right_truncatable_primes.sort(reverse=True)
    return left_right_truncatable_primes