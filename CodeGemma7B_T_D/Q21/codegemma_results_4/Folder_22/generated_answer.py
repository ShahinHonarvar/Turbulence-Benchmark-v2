def all_ints_div_by_num(nums):
    results = []
    for num in nums[10:20]:
        if num % 1 == 0:
            results.append(num)
    return results