from itertools import chain, islice

def lists_with_product_equal_n(circular_list):
    result = []
    n = len(circular_list)
    extended_list = list(chain(circular_list, circular_list[:-1]))
    for start in range(n):
        product = 1
        for end in range(start, start + n):
            product *= extended_list[end]
            if product == -5:
                sublist = extended_list[start:end + 1 if end < n else end - n + 1]
                result.append(sublist)
            if abs(product) > abs(-5) and product != 0:
                break
    return result