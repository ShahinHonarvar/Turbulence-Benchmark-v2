def sum_odd_ints_inclusive(nums):
    odd_ints = [n for n in nums[70:85] if n % 2 != 0]
    return sum(odd_ints) if odd_ints else 0