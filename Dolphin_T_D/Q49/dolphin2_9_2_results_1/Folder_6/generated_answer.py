def if_decimal_is_divisible(binary_string):
    decimal = int(binary_string, 2)
    fibo = [0, 1]
    while len(fibo) < 185:
        fibo.append(fibo[-1] + fibo[-2])
    if decimal % fibo[184] == 0:
        return True
    else:
        return False