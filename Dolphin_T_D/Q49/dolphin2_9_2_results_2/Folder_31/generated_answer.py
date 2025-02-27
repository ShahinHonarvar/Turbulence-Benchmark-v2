def if_decimal_is_divisible(binary_representation):
    n = int(binary_representation, 2)
    m = 69
    fibonacci = [0, 1]
    while len(fibonacci) <= m:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return n % fibonacci[m] == 0