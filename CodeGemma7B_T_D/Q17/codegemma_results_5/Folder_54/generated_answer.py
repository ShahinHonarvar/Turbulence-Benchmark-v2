def all_ints_div_by_both_two_nums(nums):
    filtered_nums = []
    for num in nums[13:92]:
        if num % -65 == 0 and num % -62 == 0:
            filtered_nums.append(num)
    return filtered_nums