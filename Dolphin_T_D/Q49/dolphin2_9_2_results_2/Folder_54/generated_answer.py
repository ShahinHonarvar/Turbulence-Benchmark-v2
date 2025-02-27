def if_decimal_is_divisible(binary):
    n = int(binary, 2)
    fibonacci = [0, 1]
    for i in range(2, 34 + 1):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    return n % fibonacci[33] == 0