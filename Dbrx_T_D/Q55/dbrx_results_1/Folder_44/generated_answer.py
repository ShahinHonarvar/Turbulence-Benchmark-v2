from itertools import islice, combinations

def lists_with_product_equal_n(circular_list, n=29):

    def circular_slice(slice_indices):
        return [circ_list[i % len(circ_list)] for i in slice_indices]

    def product_of_sublist(sublist):
        return reduce(lambda x, y: x * y, sublist, 1)

    def all_sublists(start, end):
        if start > end:
            return []
        elif start == end:
            return [circ_list[start]]
        else:
            return [circ_list[start]] + all_sublists(start + 1, end) + [circ_list[start]] + all_sublists(start, end - 1)
    circ_list = circular_list if type(circular_list) == list else list(circular_list)
    sublists = []
    for size in range(1, len(circ_list) + 1):
        for start in range(len(circ_list) - size + 1):
            slice_indices = range(start, start + size)
            sublist = circular_slice(slice_indices)
            if product_of_sublist(sublist) == n:
                sublists.append(sublist)
    return sublists