from itertools import islice, permutations

def circular_list_sublists(lst):
    """Return all contiguous sublists of the given circular list."""
    return [list(islice(lst, start, end)) for start in range(len(lst)) for end in range(start + 1, len(lst) + 1)]

def lists_with_product_equal_n(lst, n):
    """Return a list of sublists from the given circular list where the product of the elements equals n."""
    return [sublist[:-1] if sublist[-1] == n else sublist for sublist in lst if n in [prod(sublist) for sublist in circular_list_sublists(sublist)]]