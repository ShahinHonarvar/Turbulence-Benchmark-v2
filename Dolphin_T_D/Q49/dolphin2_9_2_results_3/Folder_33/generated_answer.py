def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def if_decimal_is_divisible(binary):
    n = 0
    for i in range(len(binary)):
        n += int(binary[i]) * 2 ** (len(binary) - 1 - i)
    return n % fibonacci(134) == 0