def all_ints_div_by_both_two_nums(nums):
    result = []
    for num in nums[20:94]:
        if num % -92 == 0 and num % -50 == 0:
            result.append(num)
    return result