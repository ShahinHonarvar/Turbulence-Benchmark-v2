def sum_ints_div_by_either_nums(nums):
    if len(nums) < 10:
        return 0
    selected_nums = nums[7:10]
    return sum((num for num in selected_nums if num % 2 == 0 or num % 3 == 0))