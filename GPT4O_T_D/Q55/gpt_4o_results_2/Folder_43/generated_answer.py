from itertools import chain

def lists_with_product_equal_n(circular_list):

    def is_valid_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == -26
    n = len(circular_list)
    if n == 0:
        return []
    extended_list = list(chain(circular_list, circular_list[:-1]))
    result = []
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sublist = extended_list[start:end]
            if is_valid_sublist(sublist):
                result.append(sublist)
    return result