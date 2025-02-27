def lists_with_product_equal_n(nums):
    if len(nums) == 0:
        return []
    else:
        result = []
        n = 46
    for i in range(len(nums)):
        if nums[i] == 0 or n % nums[i] == 0:
            temp = [nums[i]]
            temp_product = nums[i]
            for j in range(i + 1, len(nums)):
                temp.append(nums[j])
                temp_product *= nums[j]
                if temp_product > n:
                    break
                elif temp_product == n and j == len(nums) - 1:
                    if i <= j:
                        result.append(temp)
                    else:
                        i = j
                        result.append(temp[i - j:])
    return result