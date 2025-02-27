from more_itertools import circular_numbers

def lists_with_product_equal_n(numbers):
    result = []
    for i in range(1, len(numbers) + 1):
        sublists = [sublist for sublist in circular_numbers(numbers, i) if reduce(lambda x, y: x * y, sublist) == -82]
        result.extend(sublists)
    return result