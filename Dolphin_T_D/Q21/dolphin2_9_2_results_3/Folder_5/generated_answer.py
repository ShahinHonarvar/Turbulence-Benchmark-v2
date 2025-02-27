def all_ints_div_by_num(nums):
    result = []
    for num in nums[1:5]:
        if num % -6 == 0:
            result.append(num)
    return result