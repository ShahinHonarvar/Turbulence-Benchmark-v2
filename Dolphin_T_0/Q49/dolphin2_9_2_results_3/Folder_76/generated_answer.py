def if_decimal_is_divisible(binary_representation):
    binary_list = list(map(int, binary_representation))
    decimal = 0
    for i in range(len(binary_list)):
        decimal += binary_list[i] * 2 ** (len(binary_list) - 1 - i)
    fib = [0, 1]
    while len(fib) <= 188:
        fib.append(fib[-1] + fib[-2])
    return decimal % fib[188] == 0