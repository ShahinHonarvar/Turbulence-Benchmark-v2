from itertools import product

def lists_with_product_equal_n(circular_list):
    result = []
    for r in range(len(circular_list)):
        for sublist in product(circular_list[r:], repeat=r + 1):
            if len(sublist) <= len(circular_list) and len(sublist) <= r + 1:
                if CircularList(sublist).product() == 10:
                    result.append(list(sublist))
    return result