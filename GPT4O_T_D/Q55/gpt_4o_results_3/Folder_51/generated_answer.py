def lists_with_product_equal_n(nums):

    def product_of_list(lst):
        prod = 1
        for num in lst:
            prod *= num
        return prod
    result = []
    n = len(nums)
    for start in range(n):
        for end in range(start + 1, start + n + 1):
            sublist = nums[start:end % n] if end <= n else nums[start:] + nums[:end % n]
            if product_of_list(sublist) == -44:
                result.append(sublist)
    return result