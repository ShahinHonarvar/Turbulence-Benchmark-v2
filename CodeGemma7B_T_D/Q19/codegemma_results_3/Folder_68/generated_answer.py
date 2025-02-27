def all_ints_not_div_by_num(nums):
    result = []
    for num in nums[0:7]:
        if num % 7 != 0:
            result.append(num)
    return result