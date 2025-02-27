def is_decimal_divisible(binary):
    fibonacci = [0]
    for i in range(1, 74):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    decimal = int(binary, 2)
    return decimal % fibonacci[73] == 0