def sum_ints_div_by_either_nums(nums):
    filtered_nums = [num for num in nums[0:5] if num % 8 == 0 or num % -3 == 0]
    return sum(filtered_nums) if filtered_nums else 0