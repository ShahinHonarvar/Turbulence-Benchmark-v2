def lists_with_product_equal_n(nums):

    def product(lst):
        p = 1
        for i in lst:
            p *= i
        return p
    n = len(nums)
    sublists = []
    for size in range(1, n + 1):
        for i in range(n):
            if product(nums[i:i + size]) == 76:
                sublists.append(nums[i:i + size])
    return sublists