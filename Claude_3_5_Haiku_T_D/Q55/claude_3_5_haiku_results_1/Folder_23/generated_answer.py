def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            for i in range(start, end + 1):
                index = i % n
                product *= nums[index]
                sublist.append(nums[index])
            if product == -95:
                result.append(sublist)
    return result