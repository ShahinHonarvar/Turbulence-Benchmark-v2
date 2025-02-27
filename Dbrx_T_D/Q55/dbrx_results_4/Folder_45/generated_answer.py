from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):

    def circular_sublists(circular_list, start_index=0):
        for i in range(start_index, start_index + len(circular_list)):
            yield list(islice(cycle(circular_list), i, i + len(circular_list)))
    sublists = circular_sublists(circular_list)
    result = []
    for sublist in sublists:
        if len(sublist) > 1 and sublist[0] == -5:
            result.append(sublist)
        elif len(sublist) == 1:
            continue
        elif prod(sublist) == -5:
            result.append(sublist)
    return result

def prod(lst):
    product = 1
    for num in lst:
        product *= num
    return product