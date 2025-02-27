from itertools import islice

def circular_sublists(lst):
    sublists = []
    for i in range(len(lst)):
        sublist = []
        for j in range(len(lst)):
            sublist.append(lst[(i + j) % len(lst)])
        sublists.append(sublist)
    return sublists

def sublists_with_product_equal_n(lst, n):
    sublists = circular_sublists(lst)
    matching_sublists = [sublist for sublist in sublists if reduce(lambda x, y: x * y, sublist) == n]
    return matching_sublists

def lists_with_product_equal_n(lst):
    matching_sublists = sublists_with_product_equal_n(lst, 18)
    return matching_sublists