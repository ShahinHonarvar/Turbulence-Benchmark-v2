def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fibonacci = [0, 1]
    for i in range(2, 95):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return decimal % fibonacci[94] == 0