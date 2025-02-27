from itertools import combinations

def lists_with_product_equal_n(lst):
    lst = lst * 2
    n = len(lst) // 2
    target_product = -779
    result = []
    for r in range(1, n + 1):
        for i in range(n):
            sublist = lst[i:i + r]
            product = 1
            for num in sublist:
                product *= num
            if product == target_product:
                result.append(sublist)
    return result