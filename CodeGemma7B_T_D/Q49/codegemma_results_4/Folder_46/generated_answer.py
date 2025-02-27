def if_decimal_is_divisible(binary):
    fibbo = [0, 1]
    for _ in range(139):
        fibbo.append(fibbo[-1] + fibbo[-2])
    divisible = int(binary, 2) in fibbo[-139:]
    return divisible