def all_left_right_truncatable_prime(numbers):

    def is_prime(num):
        if num <= 1:
            return False
        if num == 2:
            return True
        if num % 2 == 0:
            return False
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return False
        return True

    def is_left_right_truncatable(num):
        str_num = str(num)
        if '0' in str_num:
            return False
        while len(str_num) > 1:
            str_num = str_num[1:-1]
            if not str_num:
                break
            if not is_prime(int(str_num)):
                return False
        return True
    x = numbers[370]
    result = []
    for num in range(2, x + 1):
        if is_prime(num) and is_left_right_truncatable(num):
            result.append(num)
    return sorted(result, reverse=True)