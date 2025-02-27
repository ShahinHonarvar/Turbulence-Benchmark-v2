from itertools import combinations

def lists_with_product_equal_n(circular_list):
    length = len(circular_list)
    for sublist in combinations(circular_list, length):
        product = 1
        seen_zeros = 0
        for element in sublist:
            if element == 0:
                seen_zeros += 1
            else:
                product *= element
        if not seen_zeros and product == -69:
            return [sublist]
    return []