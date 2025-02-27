def if_decimal_is_divisible(binary_str):

    def get_next_fib(num):
        if num in (0, 1):
            return num + 1
        return get_next_fib(get_next_fib(num - 1)) + get_next_fib(num - 2)
    fib_list = [get_next_fib(i) for i in range(1, 125)]
    return int(binary_str, 2) % fib_list[-1] == 0