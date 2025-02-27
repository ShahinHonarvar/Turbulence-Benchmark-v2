def if_decimal_is_divisible(binary_string):
    fibonacci = [0, 1]
    for _ in range(44):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    divisor = fibonacci[45]
    decimal_number = int(binary_string, 2)
    return decimal_number % divisor == 0