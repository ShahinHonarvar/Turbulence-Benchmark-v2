def if_decimal_is_divisible(binary_string):
    fib = [0, 1]
    for _ in range(144):
        fib.append(fib[-1] + fib[-2])
    target_fib = fib[146]
    decimal_value = int(binary_string, 2)
    return decimal_value % target_fib == 0