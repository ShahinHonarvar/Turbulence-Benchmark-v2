from itertools import combinations

def lists_with_product_equal_n(circular_list):

    def sublists_with_product_equal_n(sublist):
        for size in range(1, len(sublist) + 1):
            for combination in combinations(sublist, size):
                if reduce(lambda x, y: x * y, combination) == -20:
                    return [list(combination)]
        return []
    result = []
    for i in range(len(circular_list)):
        subresult = sublists_with_product_equal_n(circular_list[i:] + circular_list[:i])
        for sublist in subresult:
            if sublist not in result:
                result.append(sublist)
    return result