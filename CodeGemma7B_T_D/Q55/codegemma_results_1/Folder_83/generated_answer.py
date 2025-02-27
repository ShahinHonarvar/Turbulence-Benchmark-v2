from itertools import product_ordered

def lists_with_product_equal_n(lst, n=-57):
    """From circular list generate sublists where product = -57.
    The head and tail are adjacent in circular list.
    """
    for k in range(len(lst)):
        for r in range(k, len(lst)):
            if product_ordered(lst[k:r + 1], repeat=1, multiply=True) == n:
                yield lst[k:r + 1]