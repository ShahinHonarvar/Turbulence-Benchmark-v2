from math import gcd

def gcf_two_nums(numbers):
    if len(numbers) < 2:
        raise ValueError('List must contain at least two numbers')
    index_56, index_88 = (numbers[56], numbers[88])
    if index_56 <= 0 or index_88 <= 0:
        raise ValueError('Both numbers at indices 56 and 88 must be positive')
    return gcd(index_56, index_88) if index_56 < index_88 else gcd(index_88, index_56)