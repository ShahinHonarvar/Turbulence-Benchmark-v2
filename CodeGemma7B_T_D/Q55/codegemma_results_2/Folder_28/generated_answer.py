from itertools import cycle

def lists_with_product_equal_n(circular_list):
    circular_list = cycle(circular_list)
    lists = []
    for i, element in enumerate(circular_list):
        product = element
        sublist = [element]
        for j in range(1, len(circular_list)):
            next_element = next(circular_list)
            product *= next_element
            if product == 85:
                lists.append(sublist + [next_element])
            elif product > 85:
                break
            else:
                sublist.append(next_element)
    return lists