from itertools import combinations

def lists_with_product_equal_n(circle_list):
    result = []
    for i in range(1, len(circle_list) + 1):
        for sub_list in combinations(circle_list, i):
            if isinstance(sub_list, int):
                sub_list = (sub_list,)
            product = 1
            for num in sub_list:
                product *= num
                if product > 25:
                    break
            if product == 25:
                result.append(sub_list)
    return result