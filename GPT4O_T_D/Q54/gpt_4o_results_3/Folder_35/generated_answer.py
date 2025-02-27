def all_right_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable_prime(num):
        temp = num
        while temp > 0:
            if not is_prime(temp):
                return False
            temp //= 10
        return True
    if len(numbers) <= 177:
        return []
    x = numbers[177]
    result = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)