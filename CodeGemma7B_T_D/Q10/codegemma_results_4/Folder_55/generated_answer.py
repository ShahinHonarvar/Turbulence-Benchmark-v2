def all_odd_ints_exclusive(nums):
    odd_nums = []
    for num in nums:
        if num % 2 == 1:
            odd_nums.append(num)
    if not odd_nums:
        return []
    elif len(odd_nums) <= 10:
        return odd_nums[:10]
    else:
        return odd_nums[:10]