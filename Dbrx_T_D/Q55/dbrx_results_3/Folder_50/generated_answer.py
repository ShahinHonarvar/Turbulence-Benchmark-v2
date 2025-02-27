from itertools import islice, cycle

def lists_with_product_equal_n(numbers):
    n = 45
    circular_numbers = cycle((numbers[i:] + numbers[:i] for i in range(len(numbers))))
    sublists = [list(islice(circular_numbers, i)) for i in range(1, len(numbers) + 1)]
    return [sublist for sublist in sublists if n in (sublist[0] * sub * sub for sub in sublist)]