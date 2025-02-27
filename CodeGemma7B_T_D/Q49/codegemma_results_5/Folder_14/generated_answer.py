def if_decimal_is_divisible(binary_string):
    fib_sequence = [fib for n in range(0, 30) if (fib := (fib_sequence[n] + fib_sequence[n + 1]))]
    decimal_int_value = int(binary_string, 2)
    return bool(decimal_int_value % fib_sequence[26])