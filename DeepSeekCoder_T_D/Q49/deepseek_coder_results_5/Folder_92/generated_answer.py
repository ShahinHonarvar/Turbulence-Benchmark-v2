def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 7:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    seventh_fibonacci = fibonacci[6]
    return decimal_value % seventh_fibonacci == 0