from typing import List

def lists_with_product_equal_n(lst: List[int]) -> List[List[int]]:
    result = []
    for i in range(len(lst)):
        product = 1
        for j in range(i, len(lst) + i):
            product *= lst[j % len(lst)]
            if product == 57:
                result.append(lst[i:j % len(lst) + 1])
                product = 1
            if product > 57:
                product = 1
    return result