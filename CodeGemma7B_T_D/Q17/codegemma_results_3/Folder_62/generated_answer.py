def all_ints_div_by_both_two_nums(nums):
    result = []
    for num in nums[44:60]:
        nums_by_three_nine = num % 39 == 0
        nums_by_fifteen = num % 15 == 0
        if all((nums_by_fifteen, nums_by_three_nine)):
            result.append(num)
    return result