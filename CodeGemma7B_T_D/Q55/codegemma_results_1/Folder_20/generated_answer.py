from itertools import count, tee, islice

def lists_with_product_equal_n(circular_list, n=-69):
    """
    Returns a list of sublists from a circular list that have a product of n.
    """
    length = len(circular_list)
    if length == 0:
        return []
    for size in count(1):
        for start in range(length):
            sublist = circular_list[start:start + size]
            if len(sublist) != size or sublist[-1] != sublist[0] or product(sublist) != n:
                continue
            yield sublist

def product(iterable):
    """
    Returns the product of all the elements in an iterable.
    """
    product = 1
    for element in iterable:
        product *= element
    return product