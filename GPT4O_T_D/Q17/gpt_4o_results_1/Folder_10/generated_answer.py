def all_ints_div_by_both_two_nums(nums):
    result = []
    for num in nums[32:100]:
        if num % (-11 * -15) == 0:
            result.append(num)
    return result