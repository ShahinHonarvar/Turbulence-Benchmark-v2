def lists_with_product_equal_n(nums):
    n = len(nums)
    nums = nums + nums
    ans = []
    for i in range(n):
        prod = 1
        sublist = []
        for j in range(i, i + n):
            prod *= nums[j]
            sublist.append(nums[j])
            while prod > 115:
                prod /= nums[i]
                sublist.pop(0)
                i += 1
            if prod == 115:
                ans.append(sublist)
    return ans