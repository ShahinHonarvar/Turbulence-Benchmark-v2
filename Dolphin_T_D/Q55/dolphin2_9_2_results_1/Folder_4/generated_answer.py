def circular_next(lst, index):
    return lst[(index + 1) % len(lst)]

def circular_prev(lst, index):
    return lst[index - 1 % len(lst)]

def equal_91_pairs(lst):
    return [(i, j) for i in range(len(lst)) for j in range(i + 2, len(lst) + 1) if lst[i] * lst[j - 1] == 91]

def sublist_between(lst, start, end):
    return lst[start:end] + lst[end:] + lst[:start]

def get_sublists(lst):
    pair = equal_91_pairs(lst)
    if len(pair) == 0:
        return []
    sublist = []
    for i, j in pair:
        start = min(i, j)
        end = max(i, j)
        temp_lst = sublist_between(lst, start, end)
        sublist.append(temp_lst)
    return sublist

def product_equal_n(lst, n=91):
    return get_sublists(lst)