from itertools import islice

def sublists_with_product_equal_n(circular_list, n):

    def product(sublist):
        return reduce(mul, sublist, 1)

    def circular_slice(sublist):
        return [sublist[-1]] + list(sublist[0:-1]) if len(sublist) >= 2 else sublist
    all_sublists = (sublist for start in range(len(circular_list)) for sublist in [circular_list[start:start + x] for x in range(1, len(circular_list) + 1)] if start + len(sublist) <= len(circular_list))
    matching_sublists = (sublist for sublist in all_sublists if product(sublist) == n)
    unique_sublists = {tuple(sublist) for sublist in matching_sublists}
    return [circular_slice(sublist) for sublist in unique_sublists]