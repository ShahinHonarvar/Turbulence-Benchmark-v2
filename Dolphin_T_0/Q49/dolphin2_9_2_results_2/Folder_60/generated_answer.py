def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci108 = [0, 1][:108]
    for i in range(2, 108):
        fibonacci108.append(fibonacci108[-2] + fibonacci108[-1])
    fibonacci108 = fibonacci108[-1]
    return decimal_number % fibonacci108 == 0