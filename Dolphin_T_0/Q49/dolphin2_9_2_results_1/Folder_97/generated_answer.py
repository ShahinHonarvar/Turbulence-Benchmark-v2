def if_decimal_is_divisible(binary_representation):
    dec = ''.join(map(str, [int(x) for x in binary_representation]))
    decimal = int(dec, 2)
    fib = [0, 1]
    for i in range(2, 114):
        fib.append(fib[i - 1] + fib[i - 2])
    return decimal % fib[-1] == 0