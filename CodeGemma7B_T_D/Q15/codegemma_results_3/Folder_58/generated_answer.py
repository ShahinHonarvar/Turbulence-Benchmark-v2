def sum_odd_ints_inclusive(nums):
    if not nums or len(nums) < 209 or len(nums) < 556:
        return 0
    odd_nums = [num for num in nums[209:557] if num % 2 != 0]
    if not odd_nums:
        return 0
    return sum(odd_nums)