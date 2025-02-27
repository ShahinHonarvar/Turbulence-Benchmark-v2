def if_decimal_is_divisible(binary_number: str) -> bool:
    n = int(binary_number, 2)
    fibo = [0, 1]
    while len(fibo) < 78:
        fibo.append(fibo[-1] + fibo[-2])
    return n % fibo[77] == 0