def sum_odd_ints_inclusive(nums):
    odd_nums = [num for num in nums[17:79] if num % 2 != 0]
    if not odd_nums:
        return 0
    return sum(odd_nums)