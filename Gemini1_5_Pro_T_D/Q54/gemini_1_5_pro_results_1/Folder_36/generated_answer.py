def all_right_truncatable_prime(numbers):
    x = numbers[992]

    def is_right_truncatable_prime(num):
        if num <= 1:
            return False
        for i in range(1, len(str(num)) + 1):
            if not is_prime(int(str(num)[:i])):
                return False
        return True

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    result = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            result.append(i)
    return sorted(result)