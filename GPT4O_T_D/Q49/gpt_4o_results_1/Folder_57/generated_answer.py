def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    fib = [0, 1]
    for _ in range(2, 81):
        fib.append(fib[-1] + fib[-2])
    return decimal_number % fib[80] == 0