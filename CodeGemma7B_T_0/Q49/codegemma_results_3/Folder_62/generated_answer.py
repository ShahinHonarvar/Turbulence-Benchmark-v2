def if_decimal_is_divisible(binary_str):

    def get_next_fib(num):
        if num in (0, 1):
            return num + 1
        return get_next_fib(get_next_fib(num - 1)) + get_next_fib(num - 2)
    fib_num = get_next_fib(129)
    return int(binary_str, 2) % fib_num == 0