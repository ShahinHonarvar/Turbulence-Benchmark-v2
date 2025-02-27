def lists_with_product_equal_n(nums):
    result = []
    product = 1
    for i in range(len(nums)):
        product *= nums[i]
        j = i
        while product >= 54 and j >= 0:
            if product == 54:
                sublist = []
                k = i
                while k != j:
                    sublist.append(nums[k])
                    product /= nums[k]
                    k = (k - 1) % len(nums)
                sublist.append(nums[j])
                result.append(sublist)
            product /= nums[j]
            j = (j - 1) % len(nums)
    return result