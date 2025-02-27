def all_odd_ints_inclusive(nums):
    return [num for num in nums if num % 2 == 1 and 0 <= nums.index(num) <= 5]