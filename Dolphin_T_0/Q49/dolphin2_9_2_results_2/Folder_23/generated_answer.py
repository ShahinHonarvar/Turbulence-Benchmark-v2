def if_decimal_is_divisible(binary):
    decimal = 0
    power = len(binary) - 1
    for digit in binary:
        decimal += int(digit) * pow(2, power)
        power -= 1
    fib_48 = 0
    i = 0
    while i < 48:
        if i == 0:
            fib_48 = fib(i)
        else:
            fib_48 = fib(i) + fib(i - 1)
        i += 1
    return decimal % fib_48 == 0

def fib(i):
    if i < 2:
        return i
    else:
        a, b = (0, 1)
        for _ in range(2, i + 1):
            a, b = (b, a + b)
        return b