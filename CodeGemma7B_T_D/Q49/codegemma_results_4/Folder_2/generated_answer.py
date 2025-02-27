def if_decimal_is_divisible(binary_str):

    def get_fib(n):
        if n <= 1:
            return n
        return get_fib(n - 1) + get_fib(n - 2)
    binary_num = int(binary_str, 2)
    fib_num = get_fib(binary_num + 1)
    return fib_num % 125 == 0