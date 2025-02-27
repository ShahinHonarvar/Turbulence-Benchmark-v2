def all_odd_ints_inclusive(nums):
    return nums[29:80:2] if any((n % 2 for n in nums[29:80])) else []