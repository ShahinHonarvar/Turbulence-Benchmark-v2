from itertools import permutations

def lists_with_product_equal_n(circular_list):
    circular_list.append(circular_list[0])
    sublists = [circular_list[i:j] for i in range(len(circular_list)) for j in range(i + 1, len(circular_list))]
    products = [product(sublist) for sublist in sublists]
    return [sublist for sublist, product in zip(sublists, products) if product == 74]

def product(iterable):
    product = 1
    for i in iterable:
        product *= i
    return product