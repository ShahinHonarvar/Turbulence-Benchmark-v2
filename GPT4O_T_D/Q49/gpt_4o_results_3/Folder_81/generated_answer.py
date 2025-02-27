def if_decimal_is_divisible(binary_string):
    fibonacci = [0, 1]
    for _ in range(2, 98):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    fibonacci_number = fibonacci[97]
    decimal_integer = int(binary_string, 2)
    return decimal_integer % fibonacci_number == 0