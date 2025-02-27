def sum_ints_div_by_either_nums(nums):
    sum = 0
    for num in nums[93:95 + 1]:
        if num % 53 == 0 or num % 91 == 0:
            sum += num
    if not sum:
        return 0
    return sum