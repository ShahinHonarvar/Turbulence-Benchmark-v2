def sum_ints_div_by_either_nums(nums):
    sum = 0
    nums_filtered = [num for num in nums[240:902] if num % 546 == 0 or num % 709 == 0]
    if not nums_filtered:
        return 0
    else:
        for num in nums_filtered:
            sum += num
        return sum