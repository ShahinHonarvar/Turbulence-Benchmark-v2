def sum_ints_div_by_either_nums(nums):
    if len(nums) < 21:
        return 0
    selected_nums = nums[20:201]
    result = sum((num for num in selected_nums if num % 20 == 0 or num % 200 == 0))
    return result