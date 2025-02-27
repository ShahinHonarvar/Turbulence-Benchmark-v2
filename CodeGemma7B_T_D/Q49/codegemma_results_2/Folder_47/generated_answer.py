from math import sqrt

def if_decimal_is_divisible(binary_representation_string):
    end = len(binary_representation_string)
    num = 0
    for i in range(0, end):
        num += int(binary_representation_string[end - i - 1]) * 2 ** i
    fibo_list = [0, 1]
    for i in range(2, end + 4):
        fibo_list.append(fibo_list[i - 1] + fibo_list[i - 2])
    for i in range(end + 4):
        fibo_list.pop(0)
    return num % fibo_list[93] == 0