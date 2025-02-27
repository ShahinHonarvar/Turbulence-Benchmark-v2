def if_decimal_is_divisible(binary_string):
    fibonacci = [0, 1]
    for i in range(2, 110):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal_number = int(binary_string, 2)
    return decimal_number % fibonacci[109] == 0