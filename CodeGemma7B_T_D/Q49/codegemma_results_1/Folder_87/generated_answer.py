def if_decimal_is_divisible(bin_str):

    def get_fib_num(n):
        if n <= 1:
            return n
        return get_fib_num(n - 1) + get_fib_num(n - 2)
    decimal = int(bin_str, 2)
    fibonacci_index = 2
    while True:
        fibonacci_num = get_fib_num(fibonacci_index)
        if fibonacci_num == decimal:
            return True
        elif fibonacci_num > decimal:
            return False
        fibonacci_index += 1