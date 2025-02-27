def if_decimal_is_divisible(binary_number):
    decimal = int(binary_number, 2)
    fibonacci = [0, 1]
    for i in range(2, 29):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    if decimal % fibonacci[28] == 0:
        return True
    return False