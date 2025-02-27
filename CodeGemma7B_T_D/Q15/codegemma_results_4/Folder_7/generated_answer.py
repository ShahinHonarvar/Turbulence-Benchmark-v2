def sum_odd_ints_inclusive(nums):
    if not 661 <= nums[661] % 2 <= 924 >= nums[924] % 2:
        return 0
    return sum((i for i in nums[661:925] if i % 2 == 1))