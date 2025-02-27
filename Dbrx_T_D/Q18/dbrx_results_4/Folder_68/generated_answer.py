def sum_ints_div_by_either_nums(nums):
    if len(nums) < 15:
        return 0
    start_index = 7
    end_index = 7 + start_index
    total = 0
    for num in nums[start_index:end_index]:
        if num % 5 == 0 or num % 7 == 0:
            total += num
    return total