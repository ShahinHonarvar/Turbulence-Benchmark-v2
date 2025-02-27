def if_decimal_is_divisible(binary_str):
    decimal = int(binary_str, 2)
    fibs = [0, 1]
    for i in range(2, 89):
        fibs.append(fibs[i - 1] + fibs[i - 2])
    return decimal % fibs[88] == 0