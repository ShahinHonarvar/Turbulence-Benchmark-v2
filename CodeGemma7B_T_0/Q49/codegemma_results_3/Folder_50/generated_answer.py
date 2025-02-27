def if_decimal_is_divisible(binary_str):

    def get_next_fib(num):
        if num in (0, 1):
            return num
        return get_next_fib(num - 1) + get_next_fib(num - 2)

    def get_decimal(binary_str):
        return int(binary_str, 2)

    def is_divisible(num):
        fib_num = get_next_fib(num)
        return num % fib_num == 0
    if len(binary_str) < 10:
        return False
    return is_divisible(get_decimal(binary_str))