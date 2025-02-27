def if_decimal_is_divisible(binary_representation):
    dec = int(binary_representation, 2)
    i = 0
    fib1 = 0
    fib2 = 1
    if i == 0:
        fib15 = fib1
        fib1 = fib2
        fib2 = fib1 + fib2
        i += 1
        return dec % fib15 == 0
    else:
        fib2 = fib1 + fib2
        i += 1
        if i == 14:
            return dec % fib15 == 0
        else:
            fib1 = fib2
            fib2 = fib1 + fib2
            i += 1
            return if_decimal_is_divisible(binary_representation)