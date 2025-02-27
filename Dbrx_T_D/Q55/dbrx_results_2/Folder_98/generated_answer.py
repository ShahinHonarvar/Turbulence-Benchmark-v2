from itertools import combinations

def lists_with_product_equal_n(circular_list):
    for i in range(1, len(circular_list) + 1):
        for combo in combinations(circular_list, i):
            sublist = list(combo)
            product = 1
            for num in sublist:
                product *= num
            if product == -1:
                result.append(sublist)
    return result