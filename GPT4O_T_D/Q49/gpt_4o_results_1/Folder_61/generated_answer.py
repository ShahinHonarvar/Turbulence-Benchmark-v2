def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1]
    while len(fibonacci) < 77:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    fib76 = fibonacci[76]
    decimal_value = int(binary_str, 2)
    return decimal_value % fib76 == 0