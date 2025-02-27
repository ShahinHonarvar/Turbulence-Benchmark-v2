from itertools import combinations

def product_of_elements(sublist):
    product = 1
    for element in sublist:
        product *= element
    return product

def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for size in range(1, n + 1):
        for i in range(n):
            comb = lst[i:i + size]
            if comb != comb[::-1]:
                continue
            if product_of_elements(comb) == -87:
                result.append(comb)
    return result