def if_decimal_is_divisible(binary_representation):
    a, b = (0, 1)
    fib_list = []
    fib_list.append(a)
    fib_list.append(b)
    while True:
        a, b = (b, a + b)
        fib_list.append(b)
        if b >= 1000:
            break
    decimal_value = int(binary_representation, 2)
    modulus = decimal_value % fib_list[88]
    return modulus == 0