def if_decimal_is_divisible(binary_string):
    decimal_number = int(binary_string, 2)
    fibonacci = [0, 1]
    for i in range(2, 17):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    return decimal_number % fibonacci[16] == 0