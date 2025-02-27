def product(lst):
    p = 1
    for i in lst:
        p *= i
    return p

def overlap(lst1, list2):
    if len(lst1) != len(list2):
        return False
    for i in range(len(lst1)):
        if lst1[i] != list2[i]:
            return False
    return True

def lists_with_product_equal_n(lst):
    list_of_lists = []
    for i in range(len(lst)):
        for n in range(i + 1, len(lst) + 1):
            sublist = lst[i:n]
            if product(sublist) == 54:
                if sublist not in list_of_lists:
                    list_of_lists.append(sublist)
    return list_of_lists