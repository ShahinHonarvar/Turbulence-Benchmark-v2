from itertools import islice, cycle

def lists_with_product_equal_n(nums):

    def circular_sublists(nums):
        for i in range(-len(nums), 0):
            yield list(islice(cycle(nums), i, i + len(nums)))

    def product_of_sublist(sublist):
        return reduce(lambda x, y: x * y, sublist)
    return [sublist for sublist in circular_sublists(nums) if product_of_sublist(sublist) == 37]