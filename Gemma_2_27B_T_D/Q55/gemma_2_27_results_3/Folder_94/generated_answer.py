def lists_with_product_equal_n(nums):

    def product(sublist):
        result = 1
        for i in sublist:
            result *= i
        return result
    sublists = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            sublist = nums[i:j]
            if product(sublist) == -30:
                sublists.append(sublist)
    return sublists