def if_decimal_is_divisible(binary_representation):
    n = int(binary_representation, 2)
    fib = [0, 1]
    for i in range(2, 69):
        fib.append(fib[i - 1] + fib[i - 2])
    return n % fib[68] == 0