def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 9:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    ninth_fibonacci = fibonacci[8]
    return decimal_value % ninth_fibonacci == 0