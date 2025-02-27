from itertools import islice, cycle

def circular_slice(circular_list, start, end):
    return list(islice(cycle(circular_list), start, end))

def lists_with_product_equal_n(circular_list):
    result = []
    for i in range(len(circular_list)):
        sub_list = circular_list[i:i + 4]
        if reduce(lambda x, y: x * y, sub_list, 1) == -81:
            result.append(sub_list)
    return result