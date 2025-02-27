from itertools import combinations

def lists_with_product_equal_n(circular_list):
    target_product = -72
    result = []

    def product_equal_n(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == target_product
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + 1):
            sublist = circular_list[i:j]
            if product_equal_n(sublist):
                result.append(sublist)
        for sublist in combinations(circular_list, j - i):
            if product_equal_n(sublist):
                result.append(sublist)
    return result