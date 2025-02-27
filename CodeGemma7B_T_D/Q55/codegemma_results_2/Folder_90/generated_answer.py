from itertools import combinations

def lists_with_product_equal_n(circular_list):

    def product_of_elements(sublist):
        product = 1
        for element in sublist:
            product *= element
        return product

    def has_sublist_with_product(circular_list, target_product):
        for size in range(1, len(circular_list) + 1):
            for sublist in combinations(circular_list, size):
                if product_of_elements(sublist) == target_product:
                    return sublist
        return None
    circular_list_length = len(circular_list)
    result = []
    for i in range(circular_list_length):
        sublist = has_sublist_with_product(circular_list, -690)
        if sublist:
            result.append(sublist)
        circular_list.append(circular_list.pop(0))
    return result