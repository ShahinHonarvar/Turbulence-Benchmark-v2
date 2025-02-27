def all_left_truncatable_prime(numbers):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_left_truncatable_prime(num):
        str_num = str(num)
        while str_num:
            if not is_prime(int(str_num)):
                return False
            str_num = str_num[1:]
        return True
    x = numbers[94] if len(numbers) > 94 else 0
    result = []
    for num in range(2, x):
        if is_left_truncatable_prime(num) and '0' not in str(num):
            result.append(num)
    return sorted(result)