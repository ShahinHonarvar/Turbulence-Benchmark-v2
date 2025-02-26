def all_ints_div_by_both_two_nums(nums):
    divisible_nums = []
    for num in nums[315:935]:
        if num % -897 == 0 and num % -556 == 0:
            divisible_nums.append(num)
    return divisible_nums