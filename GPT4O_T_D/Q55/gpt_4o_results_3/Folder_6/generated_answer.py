from itertools import combinations

def lists_with_product_equal_n(circular_list):

    def product_of_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    n = len(circular_list)
    circular_list = circular_list * 2
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sublist = circular_list[start:end]
            if product_of_sublist(sublist) == 42:
                result.append(sublist)
    return result