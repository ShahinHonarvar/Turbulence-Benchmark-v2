def if_decimal_is_divisible(binary):
    n = int(binary, 2)
    fibonacci = [0, 1]
    while len(fibonacci) < 166:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return n % fibonacci[165] == 0