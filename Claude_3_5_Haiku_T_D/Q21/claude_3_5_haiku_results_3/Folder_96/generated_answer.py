def all_ints_div_by_num(nums):
    if len(nums) < 21:
        return []
    divisible_nums = [num for num in nums[20:21] if num % 2 == 0]
    return divisible_nums