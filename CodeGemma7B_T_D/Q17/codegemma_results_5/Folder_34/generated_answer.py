def all_ints_div_by_both_two_nums(user_nums):
    all_div_by_both_two_nums = []
    if 60 <= len(user_nums) <= 200:
        for num in user_nums[60:201]:
            if num % 9 == 0 and num % 11 == 0:
                all_div_by_both_two_nums.append(num)
    return all_div_by_both_two_nums