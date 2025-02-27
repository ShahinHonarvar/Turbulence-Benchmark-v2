def sum_ints_div_by_either_nums(nums):
    sum = 0
    nums = nums[86:91]
    for num in nums:
        if num % 71 == 0 or num % 67 == 0:
            sum += num
    return sum if sum else 0