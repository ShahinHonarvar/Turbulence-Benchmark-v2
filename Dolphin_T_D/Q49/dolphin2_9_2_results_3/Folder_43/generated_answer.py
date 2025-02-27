def if_decimal_is_divisible(n):
    decimal = int(n, 2)
    fibonacci = [0, 1]
    i = 2
    while fibonacci[i - 1] < decimal:
        fibonacci.append(fibonacci[i - 1] + fibonacci[i - 2])
        i += 1
    return decimal % fibonacci[76] == 0