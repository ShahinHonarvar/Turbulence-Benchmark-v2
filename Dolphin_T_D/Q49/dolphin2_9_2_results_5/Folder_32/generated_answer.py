def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fibonacci = [0, 1]
    for _ in range(2, 178):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return decimal % fibonacci[-1] == 0