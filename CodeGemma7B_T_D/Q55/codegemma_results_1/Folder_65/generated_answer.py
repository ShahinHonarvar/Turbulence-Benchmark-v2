from itertools import islice
from itertools import groupby

def lists_with_product_equal_n(circular_list):
    """
    Circular list is a list that can be considered as circular, meaning the head of the list is adjacent to the tail of the list. 
    """
    return [list(group) for window in windows(circular_list, range(1, len(circular_list) + 1)) for group in islice(groupby(window, key=lambda x: x[0] * x[-1]), 0, None) if group[0] == 46]

def windows(circular_list, window_sizes):
    """ circular list is a list that can be considered as circular, meaning the head of the list is adjacent to the tail of the list.

    """
    for window_size in window_sizes:
        for i in range(len(circular_list) - window_size + 1):
            yield circular_list[i:i + window_size]

def groupby(iterable, key):
    """
    Group elements of an iterable under a given key.

    key: A function which is applied to each element of the iterable.
    """
    groups = {}
    for element in iterable:
        key_value = key(element)
        groups.setdefault(key_value, []).append(element)
    return groups.values()