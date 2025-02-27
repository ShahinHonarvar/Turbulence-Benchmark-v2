from itertools import combinations

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    results = []
    for size in range(1, n + 1):
        for start in range(n):
            product = 1
            sublist = []
            for i in range(size):
                index = (start + i) % n
                product *= circular_list[index]
                sublist.append(circular_list[index])
            if product == -15:
                results.append(sublist)
    return results