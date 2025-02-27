def if_decimal_is_divisible(binary):
    fibo = [0, 1]
    while len(fibo) <= 18:
        fibo.append(fibo[-1] + fibo[-2])
    fibo_num = fibo[17]
    decimal = int(binary, 2)
    return decimal % fibo_num == 0