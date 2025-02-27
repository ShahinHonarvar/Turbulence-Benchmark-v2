def if_decimal_is_divisible(binary):
    fibonacci = [0, 1]
    for i in range(2, 28):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    n = int(binary, 2)
    return n % fibonacci[27] == 0