def sum_ints_div_by_either_nums(nums):
    if len(nums) < 695:
        return 0
    total = 0
    for num in nums[281:695]:
        if num % -722 == 0 or num % -731 == 0:
            total += num
    return total