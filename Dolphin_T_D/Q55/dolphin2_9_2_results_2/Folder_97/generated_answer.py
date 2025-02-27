def lists_with_product_equal_n(lst):
    result = []
    size = len(lst)
    for i in range(size):
        copy_lst = lst[i:] + lst[:i]
        for j in range(1, size + 1):
            tmp = copy_lst[:j]
            if j > 1 and copy_lst[j - 1] == 0:
                continue
            product = 1
            for k in tmp:
                product *= k
            if product == -938:
                result.append(lists_with_product_equal_n.sublist(tmp))
    return result

def circular_list():
    pass