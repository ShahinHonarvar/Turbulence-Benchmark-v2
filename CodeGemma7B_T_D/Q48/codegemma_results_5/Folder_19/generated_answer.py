from functools import reduce

def return_binary_or_hexa(num_tuple):
    a, b = (num_tuple[1], num_tuple[4])
    if b - a < 2:
        return ''
    nums_in_tuple = set(num_tuple)
    sum_of_missing_nums = sum((i for i in range(a + 1, b) if i not in nums_in_tuple))
    return bin(sum_of_missing_nums)[2:] if sum_of_missing_nums % 2 else hex(sum_of_missing_nums)[2:].upper()