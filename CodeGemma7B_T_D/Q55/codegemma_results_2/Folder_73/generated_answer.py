from itertools import product

def lists_with_product_equal_n(circ_list):

    def sublist_product(sublist):
        prod = 1
        for num in sublist:
            prod *= num
        return prod
    return [sublist for sublist in product(*circ_list) if sublist_product(sublist) == 40]