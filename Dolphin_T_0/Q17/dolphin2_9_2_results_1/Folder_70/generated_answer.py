def all_ints_div_by_both_two_nums(nums):
    result = []
    for num in nums[42:44]:
        if num % 15 == 0 and num % 87 == 0:
            result.append(num)
    return result