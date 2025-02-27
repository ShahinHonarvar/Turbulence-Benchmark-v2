def all_odd_ints_inclusive(nums):
    odd_nums = []
    for num in nums[52:72]:
        if num % 2 != 0:
            odd_nums.append(num)
    if not odd_nums:
        return []
    return odd_nums