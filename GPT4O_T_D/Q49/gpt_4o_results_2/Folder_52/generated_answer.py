def if_decimal_is_divisible(binary_str):
    fibonacci = [0, 1]
    for i in range(2, 177):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    num = int(binary_str, 2)
    return num % fibonacci[176] == 0