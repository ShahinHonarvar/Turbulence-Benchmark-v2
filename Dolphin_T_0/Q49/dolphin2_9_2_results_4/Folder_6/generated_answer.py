def if_decimal_is_divisible(binary_representation):
    decimal_number = int(binary_representation, 2)
    n = 185
    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return decimal_number % fib[n - 1] == 0