def product(arr):
    prod = 1
    for el in arr:
        prod *= el
    return prod

def lists_with_product_equal_n(lst):
    sublists = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if product(lst[i:j]) == -81:
                sublists.append(lst[i:j])
    return sublists