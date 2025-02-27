def all_ints_not_div_by_num(nums):
    result = []
    for num in nums[767:938]:
        if num % 593 != 0:
            result.append(num)
    return result