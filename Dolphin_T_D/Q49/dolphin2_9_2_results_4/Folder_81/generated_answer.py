def if_decimal_is_divisible(binary_representation):
    fibonacci = [0, 1]
    while fibonacci[-2] + fibonacci[-1] < int(binary_representation, 2):
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
    return fibonacci[-1] % 97 == 0