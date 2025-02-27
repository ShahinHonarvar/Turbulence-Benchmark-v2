def all_ints_div_by_num(nums):
    result = []
    for num in nums[20:201]:
        if num % 4 == 0:
            result.append(num)
    return result