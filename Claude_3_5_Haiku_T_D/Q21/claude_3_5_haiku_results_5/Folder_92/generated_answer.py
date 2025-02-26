def all_ints_div_by_num(nums):
    if not nums:
        return []
    result = []
    for num in nums[0:1]:
        if num % 1 == 0:
            result.append(num)
    return result