def if_decimal_is_divisible(binary_string):
    binary_int = int(binary_string, 2)
    fib_index = 2
    fib_num = 1
    while fib_num < binary_int:
        fib_num = fib_sequence[fib_index]
        fib_index += 1
    if fib_num % binary_int == 0:
        return True
    else:
        return False