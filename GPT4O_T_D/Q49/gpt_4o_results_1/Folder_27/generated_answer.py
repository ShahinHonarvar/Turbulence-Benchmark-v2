def if_decimal_is_divisible(binary_string):
    fibonacci = [0, 1]
    while len(fibonacci) < 88:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    fib_87 = fibonacci[87]
    decimal_number = int(binary_string, 2)
    return decimal_number % fib_87 == 0