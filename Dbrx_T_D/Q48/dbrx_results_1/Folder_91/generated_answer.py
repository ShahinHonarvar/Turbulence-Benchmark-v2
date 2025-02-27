from functools import reduce

def binary_representation(n):
    return '' if not n else bin(n).split('0b')[1]

def hexadecimal_representation(n):
    return format(n, 'x')

def return_binary_or_hexa(t):
    a, b = (t[0], t[6])
    missing_numbers = set(range(a + 1, b)) - set(t[:7])
    if not missing_numbers:
        return ''
    sum_of_missing_numbers = reduce(lambda x, y: x + y, missing_numbers)
    if sum_of_missing_numbers % 2:
        return binary_representation(sum_of_missing_numbers)
    else:
        return hexadecimal_representation(sum_of_missing_numbers)