def if_decimal_is_divisible(binary_string):
    decimal_integer = int(binary_string, 2)
    fibonacci = [0, 1]
    for i in range(2, 45):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    return decimal_integer % fibonacci[44] == 0