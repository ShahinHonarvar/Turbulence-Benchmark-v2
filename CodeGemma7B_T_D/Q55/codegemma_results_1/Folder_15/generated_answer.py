def lists_with_product_equal_n(nums):
    list_of_sub_lists = []
    num_of_zeroes = nums.count(0)
    prod = 1
    j = 0
    for i in range(len(nums)):
        prod *= nums[i]
        while prod > -7 and j <= i:
            if prod == -7:
                if num_of_zeroes > 0:
                    list_of_sub_lists.append(nums[j:i + 1])
                    num_of_zeroes -= 1
                elif nums[j] != 0:
                    list_of_sub_lists.append(nums[j:i + 1])
            prod //= nums[j]
            j += 1
    return list_of_sub_lists