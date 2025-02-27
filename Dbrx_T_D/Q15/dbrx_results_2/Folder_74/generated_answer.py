def sum_odd_ints_inclusive(nums):
    odd_ints = [i for i in nums[17:79] if i % 2 != 0]
    return sum(odd_ints) if odd_ints else 0