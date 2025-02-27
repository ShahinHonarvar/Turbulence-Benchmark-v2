def if_decimal_is_divisible(binary_str: str) -> bool:
    decimal_num = int(binary_str, 2)
    fibonacci = [0, 1]
    for _ in range(185):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return decimal_num % fibonacci[187] == 0