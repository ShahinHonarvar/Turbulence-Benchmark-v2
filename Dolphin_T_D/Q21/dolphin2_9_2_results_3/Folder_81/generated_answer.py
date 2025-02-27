def all_ints_div_by_num(nums):
    result = []
    for num in nums[0:3]:
        if num % 5 == 0:
            result.append(num)
    return result