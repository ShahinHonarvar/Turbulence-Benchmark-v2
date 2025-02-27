def if_decimal_is_divisible(binary_representation):
    fibonacci = [0]
    for i in range(1, 59):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    if int(binary_representation, 2) % fibonacci[58] == 0:
        return True
    else:
        return False