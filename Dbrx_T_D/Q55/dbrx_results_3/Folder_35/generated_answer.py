from itertools import islice
from more_itertools import windowed

def lists_with_product_equal_n(lst):

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result
    return [sublist for sublist in windowed(lst, maxlen=len(lst)) if product(sublist) == 83 and product(sublist[:-1]) <= 83 and (product(sublist[1:]) <= 83)]