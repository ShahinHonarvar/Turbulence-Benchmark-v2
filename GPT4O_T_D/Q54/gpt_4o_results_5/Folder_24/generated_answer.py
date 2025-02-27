def all_right_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_right_truncatable_prime(n):
        if not is_prime(n):
            return False
        temp = n
        while temp > 0:
            temp //= 10
            if temp > 0 and (not is_prime(temp)):
                return False
        return True
    if len(numbers) <= 65:
        return []
    x = numbers[65]
    right_truncatable_primes = [n for n in range(2, x) if is_right_truncatable_prime(n)]
    return sorted(right_truncatable_primes, reverse=True)