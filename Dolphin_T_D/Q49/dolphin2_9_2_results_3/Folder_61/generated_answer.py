def if_decimal_is_divisible(binary_rep):
    fib = [0, 1]
    decimal = 0
    for i in range(2, len(binary_rep) + 2):
        fib.append(fib[i - 1] + fib[i - 2])
    fibonacci_number = fib[-2]
    i = 0
    while i < len(binary_rep):
        decimal = decimal + int(binary_rep[i]) * pow(2, len(binary_rep) - 1 - i)
        i = i + 1
    return decimal % fibonacci_number == 0