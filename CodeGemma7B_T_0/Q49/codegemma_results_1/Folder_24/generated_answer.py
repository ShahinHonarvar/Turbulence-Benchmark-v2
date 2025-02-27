def if_decimal_is_divisible(binary_str):

    def get_next_fib(fib):
        return fib + get_next_fib(fib - 1) if fib > 1 else 1
    fib = get_next_fib(0)
    for digit in binary_str:
        if digit == '1':
            if fib % 56 == 0:
                return True
            fib = get_next_fib(fib)
    return False