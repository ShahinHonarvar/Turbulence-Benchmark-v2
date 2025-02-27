def all_even_ints_exclusive(nums):
    return [num for num in nums if num % 2 == 0 and 20 < nums.index(num) < 93]