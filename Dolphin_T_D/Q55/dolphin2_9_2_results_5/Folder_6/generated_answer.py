import itertools

def products(lst):
    n = len(lst)
    result = [1] + [0] * n
    for i in range(1, n + 1):
        result[i] = lst[i - 1] * result[i - 1]
    return result

def sublists(lst):
    products_lst = products(lst)
    n = len(lst)
    sublists = []
    for size in range(1, n + 1):
        for i in range(n):
            if lst[i] == size:
                new_sublist = lst[i:i + size]
                if new_sublist not in sublists:
                    sublists.append(new_sublist)
                else:
                    break
    return sublists

def lists_with_product_equal_n(lst):
    sublists = sublists(lst)
    n = len(sublists)
    pairs = []
    for i in range(n):
        for j in range(i + 1, n):
            if sublists[i] == sublists[j]:
                pairs.append((sublists[i], sublists[j]))
    unique_pairs = []
    for i in pairs:
        if i not in unique_pairs:
            unique_pairs.append(i)
    return_list = []
    for i in unique_pairs:
        if products(i) in [42]:
            return_list.append(i)
    return return_list