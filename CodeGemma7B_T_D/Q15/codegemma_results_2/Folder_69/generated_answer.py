def sum_odd_ints(nums):
    odd_nums = [num for num in nums[32:36] if num % 2 != 0]
    return sum(odd_nums) if odd_nums else 0