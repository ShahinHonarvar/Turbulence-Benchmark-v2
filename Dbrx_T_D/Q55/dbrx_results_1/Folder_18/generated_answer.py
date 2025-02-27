from itertools import islice, cycle

def lists_with_product_equal_n(nums, n=36):

    def circular_sublists(nums, start):
        return [nums[(start + i) % len(nums)] for i in range(len(nums))]

    def product(nums):
        total = 1
        for num in nums:
            total *= num
        return total
    sublists = []
    for i in range(len(nums)):
        sublist = circular_sublists(nums, i)
        if product(sublist) == n:
            sublists.append(sublist)
    return sublists