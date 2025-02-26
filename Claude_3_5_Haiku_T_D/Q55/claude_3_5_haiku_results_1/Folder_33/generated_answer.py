def lists_with_product_equal_n(nums):
    n = len(nums)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            for i in range(start, end + 1):
                index = i % n
                sublist.append(nums[index])
                product *= nums[index]
            if product == -115:
                result.append(sublist)
    return result