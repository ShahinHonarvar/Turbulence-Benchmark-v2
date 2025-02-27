def if_decimal_is_divisible(binary_int):

    def fib(n):
        if n in (0, 1):
            return n
        return fib(n - 1) + fib(n - 2)
    arr = [fib(i) for i in range(24)]
    return int(binary_int, 2) % arr[int(binary_int, 2).bit_length() - 24] == 0