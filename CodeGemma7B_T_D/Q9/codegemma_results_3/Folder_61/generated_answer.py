def all_odd_ints_inclusive(nums):
    odd_nums = [num for num in nums if num % 2 != 0 and 0 <= num <= 7]
    return odd_nums if odd_nums else []