from itertools import groupby, islice

def lists_with_product_equal_n(nums):

    def circular_sublists(nums):
        for i in range(len(nums)):
            yield nums[i:i + len(nums)]

    def product(sublist):
        return reduce(lambda x, y: x * y, sublist, 1)
    return [sublist for sublist in circular_sublists(nums) if product(sublist) == -22]