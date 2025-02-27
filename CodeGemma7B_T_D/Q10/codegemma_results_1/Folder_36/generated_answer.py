def all_odd_ints_exclusive(nums):
    return [num for num in nums[598:767] if num % 2 == 1 and num not in range(600, 768)]