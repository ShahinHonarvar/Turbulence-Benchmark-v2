from itertools import combinations_with_replacement

def lists_with_product_equal_n(c_list):
    total_len = len(c_list)
    results = []
    for i in range(1, total_len + 1):
        for sublist in combinations_with_replacement(c_list, i):
            product = 1
            for num in sublist:
                product *= num
            if product == 851:
                results.append(sublist)
    return results