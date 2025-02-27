from itertools import combinations

def lists_with_product_equal_n(circular_list):

    def is_contiguous(sublist):
        if len(sublist) == 1:
            return sublist[0] == -6
        product = 1
        for num in sublist:
            product *= num
            if product > 0:
                return False
        return product == -6
    result = []
    for length in range(1, len(circular_list) + 1):
        for combination in combinations(circular_list, length):
            if is_contiguous(list(combination)):
                result.append(list(combination))
    return result