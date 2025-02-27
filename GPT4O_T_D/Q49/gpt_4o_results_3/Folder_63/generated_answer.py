def if_decimal_is_divisible(binary_string):
    fibonacci = [0, 1]
    for _ in range(2, 145):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    number = int(binary_string, 2)
    return number % fibonacci[144] == 0