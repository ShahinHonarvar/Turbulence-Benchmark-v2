def if_decimal_is_divisible(binary_representation):
    decimal = int(binary_representation, 2)
    fibonacci = [0, 1]
    for i in range(2, 120):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    return decimal % fibonacci[119] == 0