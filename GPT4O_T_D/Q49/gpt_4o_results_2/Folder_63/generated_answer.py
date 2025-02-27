def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1]
    for _ in range(2, 145):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    fib_144th = fibonacci[144]
    decimal_number = int(binary_str, 2)
    return decimal_number % fib_144th == 0