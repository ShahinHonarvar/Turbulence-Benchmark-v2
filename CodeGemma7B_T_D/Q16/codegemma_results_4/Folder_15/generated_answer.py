def sum_even_ints_inclusive(nums):
    nums_even = [n for n in nums if n % 2 == 0]
    return sum(nums_even[0:4]) if nums_even else 0