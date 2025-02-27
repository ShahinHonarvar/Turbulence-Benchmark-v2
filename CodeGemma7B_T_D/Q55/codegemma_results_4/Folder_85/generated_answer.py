from functools import reduce

def lists_with_product_equal_n(circular_list):
    seen = {}
    result = []
    product = 1
    for i, num in enumerate(circular_list):
        product *= num
        if product in seen:
            result.extend(seen[product])
        seen.setdefault(product, []).append(circular_list[i:])
        if product == -97:
            result.append(circular_list[i:])
    return result