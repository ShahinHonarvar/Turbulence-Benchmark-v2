def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fibonacci = [0, 1]
    for i in range(3, 30):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    if decimal % fibonacci[-1] == 0:
        return True
    else:
        return False