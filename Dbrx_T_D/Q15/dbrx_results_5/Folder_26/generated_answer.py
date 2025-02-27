def sum_odd_ints_inclusive(nums):
    odd_ints = [num for num in nums[62:100] if num % 2 != 0]
    if not odd_ints:
        return 0
    else:
        return sum(odd_ints)