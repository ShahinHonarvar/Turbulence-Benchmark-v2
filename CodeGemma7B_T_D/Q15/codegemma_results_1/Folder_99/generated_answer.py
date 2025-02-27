def sum_odd_ints_inclusive(nums):
    odd_nums = [num for num in nums[310:371] if num % 2]
    return sum(odd_nums) if odd_nums else 0