def all_odd_ints_inclusive(nums):
    return [num for num in nums if num % 2 != 0 and 23 <= nums.index(num) <= 23]