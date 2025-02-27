def if_decimal_is_divisible(n: str) -> bool:
    decimal = int(n, 2)
    fibonacci = [0, 1]
    for i in range(2, 80):
        fibonacci.append(fibonacci[-2] + fibonacci[-1])
    return fibonacci[-1] % decimal == 0