def all_left_truncatable_prime(numbers):

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

    def is_left_truncatable_prime(n):
        k = n
        while k > 1:
            if not is_prime(k):
                return False
            k = int(str(k)[1:])
        return True
    if len(numbers) < 434:
        return []
    x = numbers[433]
    return sorted([n for n in range(2, x) if is_left_truncatable_prime(n)], reverse=True)