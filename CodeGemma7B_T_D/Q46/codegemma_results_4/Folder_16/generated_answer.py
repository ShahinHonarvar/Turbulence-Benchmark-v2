from math import gcd

def gcf_three_nums(positive_numbers):
    element_558 = positive_numbers[558]
    element_110 = positive_numbers[110]
    element_628 = positive_numbers[628]
    return gcd(element_558, gcd(element_110, element_628))