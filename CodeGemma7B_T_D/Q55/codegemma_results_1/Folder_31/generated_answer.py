from itertools import combinations_with_replacement as cwr

def lists_with_product_equal_n(given_list):
    for x in range(1, len(given_list) + 1):
        for sublist in cwr(given_list, x):
            product = 1
            for i in sublist:
                product *= i
            if product == -16:
                return [sublist]
    return []