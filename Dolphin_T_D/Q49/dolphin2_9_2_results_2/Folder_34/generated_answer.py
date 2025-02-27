def if_decimal_is_divisible(binary):
    a, b = (0, 1)
    fib = [0, 1]
    for i in range(3, 25):
        a, b = (b, a + b)
        fib.append(b)
    decimal = int(binary, 2)
    for number in fib:
        if decimal % number == 0:
            return True
    return False