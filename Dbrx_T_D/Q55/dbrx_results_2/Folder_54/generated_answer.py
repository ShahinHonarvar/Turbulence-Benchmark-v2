from itertools import combinations

def lists_with_product_equal_n(circular_list):
    sublists_with_product_equal_n = []
    for i in range(1, len(circular_list) + 1):
        for j in combinations(circular_list, i):
            if (len(j) > 1 or int(j[0]) == -17) and int(''.join(map(str, j))) == -17:
                sublists_with_product_equal_n.append(list(j))
    return sublists_with_product_equal_n