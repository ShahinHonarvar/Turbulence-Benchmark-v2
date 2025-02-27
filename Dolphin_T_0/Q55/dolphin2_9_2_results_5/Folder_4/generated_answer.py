import itertools

def lists_with_product_equal_n(lst, n=91):
    if len(lst) == 0:
        return []
    lst = lst + lst[:-1]
    sub_lists = []
    for i in range(len(lst) - 1, 0, -1):
        sub_lists += [lst[j:j + i] for j in range(len(lst) - i + 1)]
    sub_lists = list(itertools.chain(*[sub_lists[i:i + len(lst)] for i in range(0, len(sub_lists), len(lst))]))
    return [sub_list for sub_list in sub_lists if sub_list != [] and functools.reduce(lambda x, y: x * y, sub_list) == n]