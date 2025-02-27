def if_decimal_is_divisible(binary_string):
    fib = [0, 1]
    for _ in range(2, 69):
        fib.append(fib[-1] + fib[-2])
    target_number = fib[68]
    decimal_number = int(binary_string, 2)
    return decimal_number % target_number == 0