def if_decimal_is_divisible(binary_str):

    def get_fibonacci(index):
        if index in [0, 1]:
            return index
        else:
            return get_fibonacci(index - 1) + get_fibonacci(index - 2)

    def binary_to_decimal(binary_str):
        length, result = (len(binary_str), 0)
        for i in range(length):
            result += int(binary_str[length - i - 1]) * 2 ** i
        return result
    fib_num = get_fibonacci(28)
    decimal_num = binary_to_decimal(binary_str)
    return decimal_num % fib_num == 0