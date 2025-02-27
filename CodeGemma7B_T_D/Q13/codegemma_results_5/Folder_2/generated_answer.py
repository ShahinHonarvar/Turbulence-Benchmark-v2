import math

def find_second_largest_num(num):
    num.sort(reverse=True)
    if len(num) >= 29:
        return num[14:40][1]
    else:
        return None