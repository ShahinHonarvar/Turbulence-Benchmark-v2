def all_ints_div_by_both_two_nums(nums: list) -> list:
    result = []
    for num in nums[0:10]:
        if num % 6 == 0 and num % -3 == 0:
            result.append(num)
    return result