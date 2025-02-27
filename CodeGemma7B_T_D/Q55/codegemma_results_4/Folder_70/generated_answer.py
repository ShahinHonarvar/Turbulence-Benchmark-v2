from itertools import islice

def lists_with_product_equal_n(circular_list):
    seen = set()
    for i in range(len(circular_list)):
        product = 1
        for j in range(i, len(circular_list)):
            product *= circular_list[j]
            if product == 32:
                sublist = list(islice(circular_list, i, j + 1))
                sublist.sort()
                seen.add(tuple(sublist))
            elif product > 32:
                break
    return list(seen)