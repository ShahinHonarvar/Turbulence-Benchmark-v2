def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            for i in range(start, end + 1):
                curr_index = i % n
                sublist.append(nums[curr_index])
                product *= nums[curr_index]
            if product == -81:
                result.append(sublist)
    return result