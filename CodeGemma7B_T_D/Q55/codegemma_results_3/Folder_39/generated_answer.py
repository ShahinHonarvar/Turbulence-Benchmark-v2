from itertools import combinations

def lists_with_product_equal_n(circular_list):
    product = -46
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + 1):
            sublist = circular_list[i:j]
            if min(sublist) < 0 and len(sublist) <= len(circular_list):
                if product != sublist[0]:
                    return lists_with_product_equal_n(circular_list)
                for subset in combinations(sublist, len(sublist)):
                    if product == abs(subset[0] * subset[1]):
                        result.append(sublist)
    return result