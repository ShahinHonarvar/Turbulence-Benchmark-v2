def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1]
    for _ in range(2, 101):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    hundredth_fibonacci = fibonacci[100]
    decimal_value = int(binary_str, 2)
    return decimal_value % hundredth_fibonacci == 0