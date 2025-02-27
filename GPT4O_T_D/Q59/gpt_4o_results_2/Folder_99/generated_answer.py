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

    def is_left_truncatable(n):
        while n > 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    if len(numbers) < 759:
        return []
    x = numbers[758]
    result = []
    for num in range(2, x):
        if '0' not in str(num) and is_left_truncatable(num):
            result.append(num)
    return sorted(result)