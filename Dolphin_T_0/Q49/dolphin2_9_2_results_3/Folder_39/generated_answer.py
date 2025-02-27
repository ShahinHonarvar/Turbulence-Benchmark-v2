def if_decimal_is_divisible(binary_represenation):
    decimal = int(binary_represenation, 2)
    fibonacci = [0, 1]
    for i in range(2, 15):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    return decimal % fibonacci[14] == 0