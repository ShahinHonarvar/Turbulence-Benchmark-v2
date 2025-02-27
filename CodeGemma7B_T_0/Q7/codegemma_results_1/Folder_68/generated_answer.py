def all_even_ints_inclusive(nums):
    return [num for num in nums if num % 2 == 0 and 0 <= nums.index(num) <= 8]