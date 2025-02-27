def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(num):
        if '0' in str(num):
            return False
        while num > 0:
            if not is_prime(num):
                return False
            num = int(str(num)[1:]) if len(str(num)) > 1 else 0
        return True
    if len(numbers) < 95:
        return []
    x = numbers[94]
    result = []
    for num in range(2, x):
        if is_left_truncatable(num):
            result.append(num)
    return sorted(result)