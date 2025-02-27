def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    fib1, fib2 = (0, 1)
    for _ in range(114):
        fib1, fib2 = (fib2, fib1 + fib2)
    return decimal_number % fib2 == 0