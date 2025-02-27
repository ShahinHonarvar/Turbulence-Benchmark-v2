def all_ints_not_div_by_num(nums):
    result = []
    for num in nums:
        if num % 8 != 0 and 0 <= num < 5:
            result.append(num)
    return result