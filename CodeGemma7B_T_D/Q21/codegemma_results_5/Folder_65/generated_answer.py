def all_ints_div_by_num(nums):
    results = []
    for num in nums[14:57]:
        if num % -59 == 0:
            results.append(num)
    return results