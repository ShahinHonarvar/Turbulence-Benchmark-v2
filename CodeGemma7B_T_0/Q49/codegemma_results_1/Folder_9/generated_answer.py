def if_decimal_is_divisible(binary_str):

    def is_divisible(num):
        for i in range(1, 1000):
            if i * 68 in [num + i for i in range(num + 1)]:
                return True
        return False

    def get_num(binary_str):
        num = 0
        for i in range(len(binary_str)):
            num += int(binary_str[i]) * 2 ** i
        return num
    return is_divisible(get_num(binary_str))