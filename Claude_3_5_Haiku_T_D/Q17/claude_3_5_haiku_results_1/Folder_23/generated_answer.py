def all_ints_div_by_both_two_nums(nums):
    result = []
    for num in nums[69:98]:
        if num % -90 == 0 and num % -67 == 0:
            result.append(num)
    return result