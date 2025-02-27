def all_even_ints_exclusive(nums):
    return [n for n in nums if n % 2 == 0 and n not in range(8)]