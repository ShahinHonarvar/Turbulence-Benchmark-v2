def lists_with_product_equal_n(nums):
    res = []
    product = 1
    left, right = (0, 0)
    while right < len(nums):
        product *= nums[right]
        while product >= 85:
            if product == 85:
                sublist = nums[left:right + 1]
                if sublist not in res:
                    res.append(sublist)
            product //= nums[left]
            left += 1
        right += 1
    return res