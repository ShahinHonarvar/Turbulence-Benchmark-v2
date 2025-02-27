from itertools import permutations

def lists_with_product_equal_n(lst):
    result = []
    n = len(lst)
    lst += lst[:n - 1]
    for i in range(n):
        for j in range(i + 1, i + n):
            sublist = lst[i:j + 1]
            product = 1
            for num in sublist:
                product *= num
            if product == -906:
                result.append(sublist)
    return result