from itertools import combinations

def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(1, len(circular_list) + 1):
        for comb in combinations(circular_list, i):
            if len(comb) > 1:
                if {'sublist': list(comb), 'product': 32} not in result:
                    if sublists_product_equal_n(comb, 32):
                        result.append({'sublist': list(comb), 'product': 32})
            elif comb[0] == 32:
                if {'sublist': [comb[0]], 'product': 32} not in result:
                    result.append({'sublist': [comb[0]], 'product': 32})
    return [dct['sublist'] for dct in result]

def sublists_product_equal_n(sublist, n):
    if not sublist:
        return n == 1
    else:
        return sublist[0] * sublists_product_equal_n(sublist[1:], n // sublist[0]) or sublists_product_equal_n(sublist[1:], n)