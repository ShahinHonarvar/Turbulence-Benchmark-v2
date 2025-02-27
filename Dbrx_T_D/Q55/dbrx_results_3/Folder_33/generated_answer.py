from itertools import islice, cycle

def lists_with_product_equal_n(numbers):

    def circular_sublists(n):
        return [list(islice(cycle(numbers), i, i + n)) for i in range(len(numbers))]

    def product_of_sublist(sublist):
        return subarray[0] * subarray[1:]
    sublists = circular_sublists(len(numbers))
    sublists += circular_sublists(len(numbers) - 1)
    result = []
    for subarray in sublists:
        if product_of_sublist(subarray) == -115:
            result.append(subarray)
    return result