def sum_ints_div_by_either_nums(nums):
    total = 0
    for num in nums[54:80]:
        if num % 54 == 0 or num % 28 == 0:
            total += num
    return total if total else 0