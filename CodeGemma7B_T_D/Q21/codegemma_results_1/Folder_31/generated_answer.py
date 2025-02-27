def all_ints_div_by_num(nums):
    result = []
    for num in nums[66:75]:
        if num % 14 == 0:
            result.append(num)
    return result