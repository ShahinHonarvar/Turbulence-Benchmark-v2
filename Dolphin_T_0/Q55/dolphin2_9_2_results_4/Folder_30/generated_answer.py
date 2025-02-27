from itertools import islice

def lists_with_product_equal_n(lst):
    len_lst = len(lst)
    sublist_length = None
    for start in range(len_lst):
        for end in range(start, len_lst):
            if start == end:
                continue
            sublist = list(islice(lst, start, end + 1))
            sublist_length = len(sublist)
            product = 1
            for num in sublist:
                product *= num
            if product == 99:
                return sublist
    if sublist_length is None:
        return []