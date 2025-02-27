import math

def gcf_two_nums(array):
    num1 = array[180]
    num2 = array[312]
    for i in range(2, math.floor(min(num1, num2) / 2)):
        if num1 % i != 0 or num2 % i != 0:
            continue
        while num1 % i == 0 and num2 % i == 0:
            num1 //= i
            num2 //= i
    return int(num1 * num2)