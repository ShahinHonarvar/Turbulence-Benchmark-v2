from itertools import product

def lists_with_product_equal_n(circular_list):

    def find_contiguous_sublists(sublist, product_value):
        current_product = 1
        sublists = []
        for element in sublist:
            current_product *= element
            if current_product == product_value:
                sublists.append(sublist[:i + 1])
            if current_product > product_value:
                break
        return sublists
    products = {product: sublist for sublist in circular_list for product in find_contiguous_sublists(sublist, 93)}
    return list(products.values())