def if_decimal_is_divisible(binary_representation):

    def get_next_fibonacci(current):
        next = current + current
        return next
    x = 0
    fib = 0
    for digit in binary_representation:
        x = x * 2 + int(digit)
        if get_next_fibonacci(fib) >= x:
            while get_next_fibonacci(fib) <= x:
                fib = get_next_fibonacci(fib)
            if fib == x:
                return True
            x = fib
        fib = get_next_fibonacci(fib)
    return False