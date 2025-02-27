from itertools import islice, cycle

def lists_with_product_equal_n(numbers):

    def circular_sublists(circular_list):
        return [list(islice(circular_list, i)) for i in range(1, len(circular_list) + 1)]
    circular_numbers = cycle(numbers)
    sublists = circular_sublists(circular_numbers)
    result = [sublist for sublist in sublists if reduce(lambda x, y: x * y, sublist) == 28]
    return result