def all_ints_not_div_by_num(nums):
    return [num for num in nums[1:-1] if num % 10 != 0]