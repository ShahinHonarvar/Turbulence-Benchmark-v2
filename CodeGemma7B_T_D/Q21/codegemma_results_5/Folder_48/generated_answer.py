def all_ints_div_by_num(nums):
    results = []
    for num in nums[574:745]:
        if num % 649 == 0:
            results.append(num)
    return results