def product(lst):
    p = 1
    for num in lst:
        p *= num
    return p

def subsets(lst):
    subsets_lst = []
    for i in range(len(lst) + 1):
        for index in combinations(lst, i):
            subsets_lst.append(list(index))
    return subsets_lst

def lists_with_product_equal_n(lst):
    lst = lst + lst[:-1]
    subsets = subsets(lst)
    result = []
    for subset in subsets:
        if product(subset) == 40:
            result.append(subset)
    return result