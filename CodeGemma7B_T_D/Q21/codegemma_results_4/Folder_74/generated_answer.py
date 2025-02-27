def all_ints_div_by_num(nums):
    result = []
    for num in nums[62:64]:
        if num % 99 == 0:
            result.append(num)
    return result