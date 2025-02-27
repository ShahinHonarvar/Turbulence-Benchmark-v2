def if_decimal_is_divisible(binary_string):
    fibonacci = [0, 1]
    for _ in range(2, 25):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    twenty_fourth_fib = fibonacci[24]
    decimal_value = int(binary_string, 2)
    return decimal_value % twenty_fourth_fib == 0