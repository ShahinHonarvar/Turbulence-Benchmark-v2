def all_ints_div_by_num(nums):
    results = []
    for num in nums[59:98]:
        if num % -36 == 0:
            results.append(num)
    return results