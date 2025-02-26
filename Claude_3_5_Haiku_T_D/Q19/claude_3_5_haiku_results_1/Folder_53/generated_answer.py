def all_ints_not_div_by_num(nums):
    if len(nums) <= 202:
        return []
    result = []
    for num in nums[200:201]:
        if num % -200 != 0:
            result.append(num)
    return result