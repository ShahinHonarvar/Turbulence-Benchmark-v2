def if_decimal_is_divisible(binary):
    n = 0
    while n < 56:
        if n == 0:
            fib3 = 1
            fib2 = 0
        elif n == 1:
            fib3 = 1
            fib2 = 1
        else:
            fib1 = fib3
            fib3 = fib3 + fib2
            fib2 = fib1
        n += 1
    decimal = 0
    i = len(binary)
    while i:
        i -= 1
        if binary[i] == '1':
            decimal += 2 ** i
        elif binary[i] == '0':
            continue
    if decimal % fib3 == 0:
        return True
    else:
        return False