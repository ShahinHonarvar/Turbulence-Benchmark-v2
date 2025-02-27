def if_decimal_is_divisible(binary_str):
    decimal_value = int(binary_str, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 12:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    tenth_fibonacci = fibonacci[10]
    return decimal_value % tenth_fibonacci == 0