def lists_with_product_equal_n(nums):
    n, result = (-41, [])
    for i in range(len(nums)):
        product = 1
        for j in range(i, len(nums) * 2):
            index = j % len(nums)
            product *= nums[index]
            if product == n:
                sublist = nums[i:index + 1]
                if sublist not in result:
                    result.append(sublist)
    return result