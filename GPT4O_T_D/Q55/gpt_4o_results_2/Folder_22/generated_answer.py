from itertools import chain

def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []

    def product_of_list(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    extended_list = list(chain(circular_list, circular_list))
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            current_sublist = extended_list[start:end]
            if product_of_list(current_sublist) == 4:
                result.append(current_sublist[:])
    return result