def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fibonacci_97 = [0, 1]
    while len(fibonacci_97) < 97:
        fibonacci_97.append(fibonacci_97[-2] + fibonacci_97[-1])
    return decimal % fibonacci_97[-1] == 0