def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1]
    while len(fibonacci) < 128:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    fib_127th = fibonacci[127]
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_127th == 0