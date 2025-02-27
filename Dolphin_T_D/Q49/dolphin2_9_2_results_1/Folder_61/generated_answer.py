def if_decimal_is_divisible(binary_string):
    n = int(binary_string, 2)
    fibo = [0, 1]
    for i in range(2, 76):
        fibo.append(fibo[i - 1] + fibo[i - 2])
    fibo_seven_six = fibo[75]
    return n % fibo_seven_six == 0