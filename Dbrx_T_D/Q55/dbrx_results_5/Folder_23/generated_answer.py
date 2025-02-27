from itertools import islice, cycle

def lists_with_product_equal_n(numbers, target=-95):

    def contiguous_sublists(n):
        return [numbers[i:j] for i in range(len(numbers)) for j in range(i + 1, len(numbers) + 1)]

    def product_of_sublist(sublist):
        return reduce(lambda x, y: x * y, sublist, 1)
    circular_numbers = cycle(numbers)
    all_sublists = contiguous_sublists(len(numbers))
    matching_sublists = [sl for sl in all_sublists if product_of_sublist(sl) == target]
    return matching_sublists