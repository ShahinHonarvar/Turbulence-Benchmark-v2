def all_ints_div_by_both_two_nums(nums):
    result = []
    for num in nums[25:81]:
        if num % -20 == 0 and num % -26 == 0:
            result.append(num)
    return result