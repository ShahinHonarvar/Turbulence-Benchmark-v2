def all_ints_not_div_by_num(nums):
    result = []
    for num in nums[15:63]:
        if num % 34 != 0:
            result.append(num)
    return result if result else []