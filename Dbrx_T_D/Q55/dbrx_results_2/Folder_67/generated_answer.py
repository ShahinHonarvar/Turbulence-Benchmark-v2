from itertools import islice

def sublists_with_product_equal_n(lst, n=33):
    sublists = []
    for i in range(len(lst)):
        head = lst[i]
        tail = lst[:i] + lst[i + 1:]
        current_sublist = [head]
        for j in range(len(tail)):
            if product(current_sublist) * tail[j] == n:
                current_sublist.append(tail[j])
            elif product(current_sublist) * tail[j] < n:
                current_sublist.append(tail[j])
            else:
                break
        if product(current_sublist) == n:
            sublists.append(current_sublist)
    return sublists

def product(lst):
    return reduce(lambda x, y: x * y, lst, 1)