from itertools import islice

def lists_with_product_equal_n(circular_list, n):
    if not circular_list:
        return []

    def sublist_product(sublist):
        return submultiply(sublist) * (sublist[0] if n < 0 else 1)

    def continual_slice(start_index, end_index):
        sublength = end_index - start_index
        return islice(enumerate(circular_list), start_index, end_index) + ((start_index - len(circular_list), circular_list[-1]) * (n // len(circular_list)) if sublength > 0 else iter([])) + islice(enumerate(circular_list, start_index), n // sublength if sublength > 0 else 0)
    return [list(zip(*sublist))[1] for sublist in (list(continual_slice(*slice_indices)) for slice_indices in sublists_with_product_equal_n(circular_list, n)) if sublist and sublist_product(sublist) == n]

def submultiply(iterable):
    product = 1
    for element in iterable:
        product *= element
    return product

def sublists_with_product_equal_n(sequence, n):
    for i in range(1, len(sequence) + 1):
        slice_indices = (0, i)
        while slice_indices[1] <= min(i + n // submultiply(sequence[slice_indices[0]:slice_indices[1]]), len(sequence)):
            yield slice_indices
            slice_indices = (slice_indices[0] + 1, slice_indices[1] + 1)