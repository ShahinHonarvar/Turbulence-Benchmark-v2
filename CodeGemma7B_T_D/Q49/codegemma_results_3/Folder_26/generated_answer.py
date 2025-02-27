def if_decimal_is_divisible(binary):
    a, b = (0, 1)
    fib_numbers = [a]
    while b < 10 ** 7:
        fib_numbers.append(b)
        a, b = (b, a + b)
    binary_decimal = int(binary, 2)
    for num in fib_numbers:
        if binary_decimal % num == 0 and num == fib_numbers[-138]:
            return True
    return False