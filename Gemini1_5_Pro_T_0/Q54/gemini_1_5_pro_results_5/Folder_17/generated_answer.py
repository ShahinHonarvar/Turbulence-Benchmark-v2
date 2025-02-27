def all_right_truncatable_prime(numbers):
    x = numbers[36]

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable_prime(num):
        if num < 10 and is_prime(num):
            return True
        if not is_prime(num):
            return False
        return is_right_truncatable_prime(num // 10)
    result = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            result.append(num)
    result.sort(reverse=True)
    return result