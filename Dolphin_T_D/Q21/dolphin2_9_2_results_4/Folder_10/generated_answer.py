def all_ints_div_by_num(nums):
    div_by_num = []
    for num in nums[42:90]:
        if num % -59 == 0:
            div_by_num.append(num)
    return div_by_num