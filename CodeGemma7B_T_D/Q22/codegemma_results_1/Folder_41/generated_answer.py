import math

def find_sum_of_multiples(num):
    variable = num + num * num + num * num * num
    for w in range(num * num * num * num, variable + num * num * num * num, num * num * num):
        variable += w
    return variable