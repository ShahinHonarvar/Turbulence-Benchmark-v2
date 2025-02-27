from math import factorial

def find_sum_of_multiples(a):
    s = 0
    for i in range(35):
        s += a * (i + 1)
    return s