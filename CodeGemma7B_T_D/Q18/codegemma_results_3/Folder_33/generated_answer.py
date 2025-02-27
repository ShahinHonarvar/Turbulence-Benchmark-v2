def sum_ints_div_by_either_nums(nums):
    filtered_nums = [num for num in nums[281:695] if num % -722 == 0 or num % -731 == 0]
    return sum(filtered_nums) or 0