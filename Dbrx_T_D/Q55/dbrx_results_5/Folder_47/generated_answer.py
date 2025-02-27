from itertools import islice, chain

def circular_list(iterable):
    return list(chain(iterable, iterable[0]))

def lists_with_product_equal_n(numbers, target=-94):

    def product(iterable):
        return reduce(lambda x, y: x * y, iterable, 1)
    sublists = [list(islice(numbers, i, n + i)) for i in range(n) for n in range(1, len(numbers))]
    sublists.append(list(numbers))
    return [sublist for sublist in sublists if product(sublist) == target]

def sublists_with_product(numbers, target):
    n = len(numbers)
    sublists = [list(islice(numbers, i, n + i)) for i in range(n) for n in range(1, len(numbers))]
    sublists.append(list(numbers))
    return [sublist for sublist in sublists if product(sublist) == target]

def sublists_with_product_contiguous(numbers, target):
    sublists = [numbers[i:j] for i in range(len(numbers)) for j in range(i, len(numbers) + 1)]
    return [sublist for sublist in sublists if product(sublist) == target]

def list_sublists_with_product_equal_n(circular_numbers):
    return sublists_with_product_contiguous(circular_numbers, -94)