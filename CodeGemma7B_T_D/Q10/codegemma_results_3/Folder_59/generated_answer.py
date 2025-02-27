def all_odd_ints_exclusive(nums):
    odd_nums = [num for num in nums if num % 2 != 0 and 0 <= num < 10 and (num not in nums)]
    return odd_nums