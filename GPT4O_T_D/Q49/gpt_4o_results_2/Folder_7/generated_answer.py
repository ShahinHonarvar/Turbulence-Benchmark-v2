def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1]
    for _ in range(2, 161):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal_number = int(binary_str, 2)
    return decimal_number % fibonacci[160] == 0