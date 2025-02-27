from itertools import combinations

def lists_with_product_equal_n(lst):
    lst += lst
    n = len(lst)
    result = []
    for i in range(n):
        for j in range(i + 1, n):
            if i <= j:
                sublist = lst[i:j]
                product = 1
                for num in sublist:
                    product *= num
                if product == 13:
                    result.append(sublist)
    return result