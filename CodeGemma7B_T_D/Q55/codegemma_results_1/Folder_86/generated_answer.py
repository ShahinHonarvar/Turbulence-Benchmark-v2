from itertools import cycle

def lists_with_product_equal_n(circular_list):
    product = -779
    result = []
    for shift in range(len(circular_list)):
        for sublist in [circular_list[i:] + circular_list[:i] for i in range(len(circular_list))]:
            if sum(sublist) == 0 and all((x * y == 1 for x, y in zip(sublist, sublist[1:] + sublist[:1]))):
                result.append(sublist)
    return result