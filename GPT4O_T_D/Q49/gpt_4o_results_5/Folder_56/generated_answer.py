def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1]
    for _ in range(2, 85):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    fib_84 = fibonacci[84]
    decimal_value = int(binary_str, 2)
    return decimal_value % fib_84 == 0