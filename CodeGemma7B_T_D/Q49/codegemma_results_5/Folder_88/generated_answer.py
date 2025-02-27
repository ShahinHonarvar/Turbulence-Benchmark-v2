def if_decimal_is_divisible(fib_binary):
    fib_num = int(fib_binary, 2)
    fib_index = next((i for i, num in enumerate(fibonacci) if num == fib_num), None)
    return fib_index is not None and fib_index % 49 == 0