def lists_with_product_equal_n(nums):
    length = len(nums)
    for i in range(length):
        j = i + 1
        while j < length:
            product = nums[i]
            sublist = [nums[i]]
            while (j + 1) % length != i and product == 100:
                product *= nums[(j + 1) % length]
                sublist.append(nums[(j + 1) % length])
                j += 1
            if product == 100:
                return sublist
            j += 1
    return []