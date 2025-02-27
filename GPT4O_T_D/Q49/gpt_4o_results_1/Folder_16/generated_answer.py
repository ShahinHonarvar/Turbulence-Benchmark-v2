def if_decimal_is_divisible(binary_string):
    fibonacci = [0, 1]
    for i in range(2, 129):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    fib_128th = fibonacci[127]
    decimal_value = int(binary_string, 2)
    return decimal_value % fib_128th == 0