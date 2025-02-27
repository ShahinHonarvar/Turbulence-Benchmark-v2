def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fib_45 = fibonacci(45)
    if decimal % fib_45 == 0:
        return True
    else:
        return False