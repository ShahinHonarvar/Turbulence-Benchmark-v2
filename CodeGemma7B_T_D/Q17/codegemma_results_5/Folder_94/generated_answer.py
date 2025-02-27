def all_ints_div_by_both_two_nums(nums):
    result = []
    for num in nums[93:94 + 1]:
        if num % -53 == 0 and num % -91 == 0:
            result.append(num)
    return result