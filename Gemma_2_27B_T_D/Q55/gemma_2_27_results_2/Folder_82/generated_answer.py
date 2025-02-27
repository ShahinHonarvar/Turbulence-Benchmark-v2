def lists_with_product_equal_n(nums):

    def product(sublist):
        p = 1
        for num in sublist:
            p *= num
        return p
    result = []
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if product(nums[i:j + 1]) == 8:
                result.append(nums[i:j + 1])
    return result