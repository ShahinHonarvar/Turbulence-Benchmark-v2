def if_decimal_is_divisible(binary):
    decimal = int(binary, 2)
    fibo = [0, 1]
    while len(fibo) < 19:
        fibo.append(fibo[-1] + fibo[-2])
    return decimal % fibo[-1] == 0