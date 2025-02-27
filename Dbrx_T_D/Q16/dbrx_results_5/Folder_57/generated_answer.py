def sum_even_ints_inclusive(nums):
    start, end = (27, 55)
    if len(nums) <= end:
        return 0
    return sum((x for x in nums[start:end + 1] if x % 2 == 0))