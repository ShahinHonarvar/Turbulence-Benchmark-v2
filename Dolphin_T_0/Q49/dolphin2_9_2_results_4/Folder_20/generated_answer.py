def if_decimal_is_divisible(binary_representation):
    decimal_integer = int(binary_representation, base=2)
    fib1, fib2 = (0, 1)
    for _ in range(100):
        fib1, fib2 = (fib2, fib1 + fib2)
    return decimal_integer % fib2 == 0