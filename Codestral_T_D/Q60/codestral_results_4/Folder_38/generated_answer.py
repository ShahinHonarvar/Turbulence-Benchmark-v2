def all_left_right_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        while num >= 10:
            num = int(str(num)[1:])
            if not is_prime(num):
                return False
        return True

    def is_right_truncatable_prime(num):
        while num >= 10:
            num = int(str(num)[:-1])
            if not is_prime(num):
                return False
        return True
    x = numbers[28]
    result = []
    for num in range(2, x + 1):
        if '0' not in str(num) and is_prime(num) and is_left_truncatable_prime(num) and is_right_truncatable_prime(num):
            result.append(num)
    return sorted(result)