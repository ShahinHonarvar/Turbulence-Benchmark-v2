from itertools import islice, cycle

def lists_with_product_equal_n(numbers, target=-57):
    if not numbers:
        return []
    circular_numbers = list(numbers)
    for i in range(len(numbers)):
        circular_numbers.append(circular_numbers[i])
    result = []
    for slice_length in range(1, len(circular_numbers) + 1):
        for sublist in window(circular_numbers, slice_length):
            if product(sublist) == target:
                result.append(list(sublist))
    return result

def window(seq, n):
    """Returns a sliding window (of width n) over data from the iterable"""
    '   s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...                   '
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result
    for elem in it:
        result = result[1:] + (elem,)
        yield result

def product(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result