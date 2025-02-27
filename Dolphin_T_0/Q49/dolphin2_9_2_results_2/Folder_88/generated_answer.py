def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    n1 = n2 = 1
    fibonacci = [0, 1]
    while len(fibonacci) < 49:
        n = n1 + n2
        fibonacci.append(n)
        n1, n2 = (n2, n)
    if decimal % fibonacci[48] == 0:
        return True
    else:
        return False