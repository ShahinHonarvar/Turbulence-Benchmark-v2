def if_decimal_is_divisible(binary_representation):
    n = 0
    for i in range(len(binary_representation)):
        n = n * 2 + int(binary_representation[i])
    fibonacci = [0, 1]
    while fibonacci[-1] <= n:
        fibonacci.append(fibonacci[-1] + fibonacci[-2])
    return n % fibonacci[3] == 0