def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = [nums[i % n] for i in range(start, end + 1)]
            product = 1
            for num in sublist:
                product *= num
            if product == 8:
                result.append(sublist)
    return result