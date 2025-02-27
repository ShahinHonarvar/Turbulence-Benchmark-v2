def lists_with_product_equal_n(nums: circular):
    n = -115
    product = 1
    lists = []
    count = 0
    for num in nums:
        count += 1
        product *= num
        if product == n:
            lists.append(nums[i:j + 1])
        elif product > n:
            while product > n and i < j and (j < count - 1):
                product //= nums[i]
                i += 1
            if product == n:
                lists.append(nums[i:j + 1])
    return lists