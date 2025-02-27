def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    i = 55
    while True:
        if i < 130:
            fib = fib[-2] + fib[-1]
        elif i == 130:
            return decimal_number % fib == 0
        else:
            fib = fib[-1]
        if fib > decimal_number:
            return False
        i += 1