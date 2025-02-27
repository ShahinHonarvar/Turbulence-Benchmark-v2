from itertools import chain

def return_binary_or_hexa(input_tuple):
    a = input_tuple[20]
    b = input_tuple[93]
    if a + 1 >= b - 1:
        return ''
    missing_numbers = set(range(a + 1, b)) - set(chain(*input_tuple[20:94]))
    if not missing_numbers:
        return ''
    sum_of_missing = sum(missing_numbers)
    if sum_of_missing % 2:
        return bin(sum_of_missing)[2:]
    else:
        return hex(sum_of_missing).split('x')[-1].upper()