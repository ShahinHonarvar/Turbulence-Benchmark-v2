from itertools import combinations

def lists_with_product_equal_n(circular_list):

    def product_of_list(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    n = len(circular_list)
    extended_list = circular_list * 2
    valid_sublists = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sublist = extended_list[start:end]
            if product_of_list(sublist) == -76:
                valid_sublists.append(sublist)
    return valid_sublists