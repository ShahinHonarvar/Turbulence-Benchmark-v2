def all_odd_ints_inclusive(nums):
    odd_nums = []
    for num in nums:
        if num % 2 != 0:
            if num >= 31 and num <= 72:
                odd_nums.append(num)
    if not odd_nums:
        return []
    return odd_nums