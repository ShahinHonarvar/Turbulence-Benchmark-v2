def all_ints_div_by_both_two_nums(nums):
    if len(nums) < 2:
        return []
    first_num = nums[0]
    second_num = nums[1]
    return [num for num in nums[0:2] if num % first_num == 0 and num % second_num == 0]