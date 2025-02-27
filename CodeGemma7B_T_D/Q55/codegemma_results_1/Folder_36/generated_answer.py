from itertools import combinations

def lists_with_product_equal_n(circular_list):
    results = []
    indexes = range(len(circular_list))
    for r in range(1, len(circular_list)):
        for i in indexes:
            product = circular_list[i]
            sublist = [circular_list[i]]
            for j in range(1, r):
                index = (i + j) % len(circular_list)
                product *= circular_list[index]
                sublist.append(circular_list[index])
            if product == 714:
                results.append(sublist)
    return results