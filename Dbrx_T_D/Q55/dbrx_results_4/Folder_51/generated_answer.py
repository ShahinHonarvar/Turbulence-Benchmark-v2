from itertools import combinations

def lists_with_product_equal_n(circular_list):
    sublists = []
    for length in range(1, len(circular_list) + 1):
        for combo in combinations(circular_list, length):
            if len(circular_list) > 3 and -44 in combo:
                sublists.append(list(combo))
            elif len(circular_list) <= 3 and -44 in combo and any((-44 / is_divisible for is_divisible in combo if is_divisible != 0)):
                sublists.append(list(combo))
    return sublists