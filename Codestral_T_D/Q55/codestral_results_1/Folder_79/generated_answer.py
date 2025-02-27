from itertools import combinations

def lists_with_product_equal_n(lst):
    double_lst = lst + lst
    result = []
    for r in range(1, len(lst) + 1):
        for i in range(len(lst)):
            sublist = double_lst[i:i + r]
            product = 1
            for num in sublist:
                product *= num
            if product == -83:
                result.append(sublist)
    return result