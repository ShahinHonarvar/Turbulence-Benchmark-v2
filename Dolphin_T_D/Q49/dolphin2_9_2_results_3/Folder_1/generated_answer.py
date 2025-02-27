def if_decimal_is_divisible(binary_string):
    number = int(binary_string, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 90:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return number % fibonacci[89] == 0