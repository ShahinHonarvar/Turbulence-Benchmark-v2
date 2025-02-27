from itertools import combinations_with_replacement

def lists_with_product_equal_n(circular_list):
    product = 29
    result = []
    for i in range(len(circular_list)):
        for j in range(i, len(circular_list)):
            sublist = circular_list[i:j + 1]
            if len(set(sublist)) != len(sublist):
                continue
            if product == 1:
                result.append(sublist)
            elif product % product_of_sublist(circular_list, sublist) == 0:
                result.append(sublist)
    return result

def product_of_sublist(circular_list, sublist):
    """Multiplies all elements in a sublist in a circular list."""
    product = 1
    for element in sublist:
        product *= element
    if sublist[0] < sublist[-1]:
        product *= circular_list[0:sublist[0]]
    return product