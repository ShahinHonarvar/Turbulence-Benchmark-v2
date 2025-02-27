def all_ints_div_by_both_two_nums(nums):
    result = []
    for num in nums[40:201]:
        if num % 21 == 0 and num % 71 == 0:
            result.append(num)
    return result