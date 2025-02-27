import math

def gcf_three_nums(numbers):
    if len(numbers) < max(944, 814, 865) + 1:
        raise IndexError('List does not contain sufficient elements.')
    num1 = numbers[944]
    num2 = numbers[814]
    num3 = numbers[865]
    return math.gcd(math.gcd(num1, num2), num3)