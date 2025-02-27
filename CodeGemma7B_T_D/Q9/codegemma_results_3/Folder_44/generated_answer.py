def all_odd_ints_inclusive(nums):
    all_odd_nums = []
    for num in nums[13:69]:
        if num % 2 != 0:
            all_odd_nums.append(num)
    if not all_odd_nums:
        return []
    return all_odd_nums