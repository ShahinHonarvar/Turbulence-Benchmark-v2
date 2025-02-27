from math import gcd

def gcf_three_nums(numbers):
    n1, n2, n3 = (numbers[84], numbers[35], numbers[53])
    return get_greatest_common_factor(n1, n2, n3)

def get_greatest_common_factor(num1, num2, num3):

    def get_gcd(a, b):
        while b != 0:
            a, b = (b, a % b)
        return a
    return get_gcd(get_gcd(num1, num2), num3)