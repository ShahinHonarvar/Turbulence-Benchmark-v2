def all_even_ints_inclusive(nums):
    return [num for num in nums if 100 <= nums.index(num) <= 200 and num % 2 == 0]