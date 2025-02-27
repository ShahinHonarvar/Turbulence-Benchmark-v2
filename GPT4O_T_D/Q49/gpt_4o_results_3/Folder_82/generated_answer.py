def if_decimal_is_divisible(binary_string):
    num = int(binary_string, 2)
    fibo = [0, 1]
    for i in range(2, 100):
        fibo.append(fibo[i - 1] + fibo[i - 2])
    return num % fibo[99] == 0