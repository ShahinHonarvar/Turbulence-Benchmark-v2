from itertools import islice

def lists_with_product_equal_n(circular_list):
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list)):
            product = circular_list[i]
            for k in islice(circular_list, j + 1, j + 1 + (j - i)):
                product *= k
            if product == 632:
                return [circular_list[i:j + 1]]
    return []