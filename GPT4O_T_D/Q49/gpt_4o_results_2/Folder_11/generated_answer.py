def if_decimal_is_divisible(binary_str):
    decimal_number = int(binary_str, 2)
    fibonacci = [0, 1]
    for _ in range(15):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return decimal_number % fibonacci[16] == 0