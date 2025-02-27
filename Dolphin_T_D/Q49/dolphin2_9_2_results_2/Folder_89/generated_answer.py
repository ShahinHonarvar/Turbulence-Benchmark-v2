def if_decimal_is_divisible(binary_rep):
    fibonacci = [0, 1]
    for i in range(2, 127):
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
    binary = int(binary_rep, 2)
    return binary % fibonacci[126] == 0