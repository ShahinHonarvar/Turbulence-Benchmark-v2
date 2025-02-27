def if_decimal_is_divisible(binary_rep):
    fibonacci = [0, 1]
    for i in range(2, 120):
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    n = int(binary_rep, 2)
    if n % fibonacci[119] == 0:
        return True
    else:
        return False