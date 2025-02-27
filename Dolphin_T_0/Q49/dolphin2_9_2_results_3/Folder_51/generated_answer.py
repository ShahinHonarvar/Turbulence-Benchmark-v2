def if_decimal_is_divisible(binary_representation):
    fib = [0, 1]
    decimal = 0
    for index in range(len(binary_representation)):
        digit = int(binary_representation[-(index + 1)])
        decimal += digit * 2 ** index
    i = 2
    while len(fib) < 17:
        fib.append(fib[i - 1] + fib[i - 2])
        i += 1
    if decimal % fib[16] == 0:
        return True
    else:
        return False