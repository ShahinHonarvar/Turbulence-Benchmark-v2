def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fibonacci = [0, 1]
    for i in range(2, 168):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    return decimal % fibonacci[167] == 0