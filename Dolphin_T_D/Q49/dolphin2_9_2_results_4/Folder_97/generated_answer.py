def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    n = 0
    fib1 = 0
    fib2 = 1
    while n < 113:
        fib_sum = fib1 + fib2
        fib1 = fib2
        fib2 = fib_sum
        n += 1
    return decimal % fib2 == 0