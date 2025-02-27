def all_ints_div_by_both_two_nums(nums):
    div_by_both = []
    for num in nums[38:53]:
        if num % -41 == 0 and num % -47 == 0:
            div_by_both.append(num)
    return div_by_both