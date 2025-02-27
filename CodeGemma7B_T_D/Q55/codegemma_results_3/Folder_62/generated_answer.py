from itertools import product

def lists_with_product_equal_n(circular_list):
    products = []
    for length in range(1, len(circular_list) + 1):
        for indices in product(range(len(circular_list)), repeat=length):
            product_of_indices = 1
            for index in indices:
                product_of_indices *= circular_list[index]
            if product_of_indices == 100:
                sublist = [circular_list[index] for index in indices]
                products.append(sublist)
    return products