from functools import reduce
from itertools import islice

def lists_with_product_equal_n(given_list):
    try:

        def product_of_list(list_arg):
            return reduce(lambda x, y: x * y, list_arg)
        result = []
        for idx in range(len(given_list)):
            for sublist_size in range(idx + 2, 0, -1):
                sublist = list(islice(given_list, idx, idx + sublist_size))
                if product_of_list(sublist) == 415:
                    result.append(sublist)
        return result
    except ZeroDivisionError:
        return []