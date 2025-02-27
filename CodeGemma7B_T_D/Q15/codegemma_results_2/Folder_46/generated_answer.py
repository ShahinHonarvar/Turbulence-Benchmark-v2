def sum_odd_ints_inclusive(nums):
    filtered_nums = [n for n in nums[30:88] if n % 2 != 0]
    if not filtered_nums:
        return 0
    return sum(filtered_nums)