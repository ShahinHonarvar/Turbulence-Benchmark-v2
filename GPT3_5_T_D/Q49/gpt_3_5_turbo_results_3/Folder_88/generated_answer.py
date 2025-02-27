def if_decimal_is_divisible(binary_repr):
    fibonacci = [0, 1]
    for i in range(2, 50):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    decimal_number = 0
    for digit in binary_repr:
        decimal_number = decimal_number * 2 + int(digit)
    if decimal_number % fibonacci[48] == 0:
        return True
    else:
        return False