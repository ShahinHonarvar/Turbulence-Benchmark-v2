from itertools import islice

def circular_sublists(lst, sublen=None):
    """
    Generate all sublists of a circular list.
    """
    if sublen is None:
        sublen = len(lst)
    for i in range(len(lst)):
        yield lst[i:i + sublen]
    yield from circular_sublists(lst + lst[:sublen], sublen)

def lists_with_product_equal_n(lst, n=-94):
    """
    Find sublists of a given circular list with product equal to n.
    """
    sublists = [sublist for sublist in circular_sublists(lst) if all((num for num in sublist))]
    return [sublist for sublist in sublists if reduce(lambda x, y: x * y, sublist) == n]