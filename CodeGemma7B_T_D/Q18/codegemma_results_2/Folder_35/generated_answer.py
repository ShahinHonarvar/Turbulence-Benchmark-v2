def sum_ints_div_by_either_nums(nums):
    sum = 0
    for num in nums[77:88]:
        if num % 23 == 0 or num % 57 == 0:
            sum += num
    return sum if sum > 0 else 0