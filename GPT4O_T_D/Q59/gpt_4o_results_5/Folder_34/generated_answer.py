def all_left_truncatable_prime(numbers):
    if len(numbers) < 19:
        return []
    x = numbers[18]

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

    def is_left_truncatable(n):
        factor = 10
        while n:
            if not is_prime(n) or '0' in str(n):
                return False
            n %= factor
            factor *= 10
        return True
    result = []
    for number in range(2, x):
        if is_left_truncatable(number):
            result.append(number)
    return sorted(result, reverse=True)