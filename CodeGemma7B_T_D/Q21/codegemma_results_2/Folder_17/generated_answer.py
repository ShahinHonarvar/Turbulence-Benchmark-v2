def all_ints_div_by_num(nums):
    result = []
    for num in nums[33:36]:
        if num % 91 == 0:
            result.append(num)
    return result