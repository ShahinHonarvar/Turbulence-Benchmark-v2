def all_left_right_truncatable_prime(numbers):
    x = numbers[24]
    result = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if '0' in str(n):
            return False
        num = str(n)
        for i in range(1, len(num)):
            if not is_prime(int(num[i:])) or not is_prime(int(num[:-i])):
                return False
        return True
    for i in range(2, x + 1):
        if is_truncatable(i):
            result.append(i)
    return result