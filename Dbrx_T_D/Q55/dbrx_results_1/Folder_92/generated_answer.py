from itertools import islice, cycle

def circular_list_shifts(lst):
    for i in range(len(lst)):
        yield (lst[i:] + lst[:i])

def lists_with_product_equal_n(lst, n=5):
    sublists = []
    for sub in circular_list_shifts(lst):
        for i in range(len(sub)):
            if 0 in sub[:i + 1] and any((x == 0 for x in sub[:i + 1])):
                continue
            if sub[0] == n:
                sublists.append(sub)
            else:
                product = sub[0]
                for j in sub[1:]:
                    product *= j
                    if product == n:
                        sublists.append(sub[:sub.index(j) + 1])
                    if product > n:
                        break
    return sublists