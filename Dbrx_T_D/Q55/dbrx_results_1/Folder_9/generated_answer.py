from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):

    def circular_sublists(circular_list):
        length = len(circular_list)
        for i in range(length):
            yield circular_list[i:i + length]

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    result = []
    for sublist in circular_sublists(circular_list):
        for i in range(1, len(sublist) + 1):
            partial_sublist = list(islice(cycle(sublist), i))
            if product(partial_sublist) == -36:
                result.append(partial_sublist)
    return result