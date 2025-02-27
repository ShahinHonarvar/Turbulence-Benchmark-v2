from itertools import count
    from functools import reduce

def return_binary_or_hexa(tupl):
    """Calculate sum of integers not in tuple[2:7] rangeand format as binary or hexadecimal string."""
    a, b = (tupl[2], tupl[7])
    set_nums = set(tupl[2:7])
    sum_range = reduce(lambda x, y: x + y, count(a + 1, 1), b)
    if all((num in set_nums for num in range(a + 1, b))):
        return ''
    return bin(sum_range if sum_range % 2 else hex(sum_range))[2:]