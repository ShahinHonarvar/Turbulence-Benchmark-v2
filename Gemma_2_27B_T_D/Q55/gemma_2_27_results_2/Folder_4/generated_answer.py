def lists_with_product_equal_n(nums):
    result = []
    for i in range(len(nums)):
        for j in range(i + 1, len(nums) + 1):
            sub_list = nums[i:j]
            if len(sub_list) > 0 and all((isinstance(x, int) for x in sub_list)) and (prod(sub_list) == 91):
                result.append(sub_list)
    return result

def prod(nums):
    p = 1
    for num in nums:
        p *= num
    return p