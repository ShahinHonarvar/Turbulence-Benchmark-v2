def all_odd_ints_inclusive(nums):
    odd_nums = [num for num in nums[37:77] if num % 2 != 0]
    return odd_nums if odd_nums else []