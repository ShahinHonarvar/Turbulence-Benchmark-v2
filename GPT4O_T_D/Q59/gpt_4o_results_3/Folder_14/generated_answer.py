def all_left_truncatable_prime(numbers):

    def is_prime(n):
        if n <= 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        if '0' in str(n):
            return False
        while n > 0:
            if not is_prime(n):
                return False
            n = int(str(n)[1:]) if len(str(n)) > 1 else 0
        return True
    x = numbers[78]
    result = []
    for num in range(2, x):
        if is_left_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)