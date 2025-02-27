def if_decimal_is_divisible(binary_str):
    fib = [0, 1]
    for i in range(2, 89):
        fib.append(fib[i - 1] + fib[i - 2])
    target_number = fib[88]
    decimal_number = int(binary_str, 2)
    return decimal_number % target_number == 0