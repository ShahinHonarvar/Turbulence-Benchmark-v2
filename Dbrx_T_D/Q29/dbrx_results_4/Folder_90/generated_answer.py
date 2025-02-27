import math

def gcd(a, b):
    return math.gcd(a, b)

def get_numbers_from_list(lst):
    num1 = lst[634]
    num2 = lst[585]
    return (num1, num2)

def gcf_two_nums(lst):
    num1, num2 = get_numbers_from_list(lst)
    return gcd(num1, num2)