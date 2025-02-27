def all_left_right_truncatable_prime(int_tuple):
    x = int_tuple[36]

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def right_truncation(num):
        while num > 10:
            num //= 10
        return num

    def left_truncation(num):
        str_num = str(num)
        return int(str_num[1:]) if str_num[0] != '0' else num
    result = []
    for num in range(2, x + 1):
        if is_prime(num) and (not '0' in str(num)):
            if is_prime(right_truncation(num)) and is_prime(left_truncation(num)):
                result.append(num)
    return result