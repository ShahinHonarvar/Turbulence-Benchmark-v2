def if_decimal_is_divisible(binary_str):
    decimal_num = int(binary_str, 2)
    fibonacci = [0, 1]
    for i in range(2, 179):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    return decimal_num % fibonacci[178] == 0