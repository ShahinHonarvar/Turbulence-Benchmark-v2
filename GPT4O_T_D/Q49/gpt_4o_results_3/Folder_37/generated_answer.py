def if_decimal_is_divisible(binary_string):
    fibonacci = [0, 1]
    for _ in range(2, 46):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    decimal_number = int(binary_string, 2)
    return decimal_number % fibonacci[45] == 0