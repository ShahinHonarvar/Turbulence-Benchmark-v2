def lists_with_product_equal_n(circular_list):
    extended_list = circular_list + circular_list
    result = []
    for length in range(1, len(circular_list) + 1):
        for i in range(len(circular_list)):
            sublist = extended_list[i:i + length]
            if product(sublist) == -46:
                result.append(sublist)
    result = [list(x) for x in set((tuple(sorted(sublist)) for sublist in result))]
    return result

def product(lst):
    p = 1
    for i in lst:
        p *= i
    return p