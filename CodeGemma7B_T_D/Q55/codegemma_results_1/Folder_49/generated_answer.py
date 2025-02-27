from itertools import islice

def lists_with_product_equal_n(circular_list):
    for i in range(len(circular_list)):
        for j in range(i + 2, len(circular_list) + i + 2):
            sublist = list(islice(circular_list, i, j))
            product = 1
            for k in sublist:
                product *= k
            if product == -61:
                return [sublist]
    return []