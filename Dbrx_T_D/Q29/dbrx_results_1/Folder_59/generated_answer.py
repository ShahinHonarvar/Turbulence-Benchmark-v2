import math

def gcf_two_nums(numbers):
    if len(numbers) < 9:
        return 'The list does not have enough elements'
    else:
        a = numbers[3]
        b = numbers[8]
        gcd_value = math.gcd(a, b)
        return gcd_value