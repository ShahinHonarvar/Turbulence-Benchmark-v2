def all_even_ints_exclusive(nums):
    return [num for num in nums if 7 < nums.index(num) < 9 and num % 2 == 0]