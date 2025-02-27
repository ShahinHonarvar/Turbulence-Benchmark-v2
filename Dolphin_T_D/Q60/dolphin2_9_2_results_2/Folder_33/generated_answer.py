def all_left_right_truncatable_prime(numbers):

    def check(n):
        if n < 10:
            return n in [2, 3, 5, 7]
        return n % 10 in [2, 3, 5, 7] and n not in [2, 3, 5, 7] and check(n // 10)

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2 or n == 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i = i + 6
        return True
    x = numbers[945]
    left_right_truncatable_primes = [i for i in range(x + 1, 0, -1) if is_prime(i) and check(i)]
    return left_right_truncatable_primes