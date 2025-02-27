def all_ints_div_by_num(nums):
    result = []
    for num in nums[18:94]:
        if num % 85 == 0:
            result.append(num)
    return result if result else []