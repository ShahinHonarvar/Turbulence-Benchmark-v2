def all_right_truncatable_prime(numbers):
    x = numbers[35]

    def is_right_truncatable_prime(num):
        if num <= 1:
            return False
        for i in range(len(str(num))):
            if not is_prime(int(str(num)[:len(str(num)) - i])):
                return False
        return True

    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True
    result = []
    for num in range(2, x):
        if is_right_truncatable_prime(num):
            result.append(num)
    result.sort(reverse=True)
    return result