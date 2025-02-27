from itertools import islice

def lists_with_product_equal_n(circular_list):

    def product(iter_):
        s = 1
        for element in iter_:
            s *= element
        return s
    for sublist_size in range(2, len(circular_list) + 1):
        for i in range(len(circular_list) - sublist_size + 1):
            sublist = circular_list[i:i + sublist_size]
            if product(sublist) == 43:
                return sublist
    return []