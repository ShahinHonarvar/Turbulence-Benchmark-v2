def sum_odd_ints_inclusive(nums):
    start = 62
    end = 99
    odd_nums = [num for num in nums[start:end + 1] if num % 2 != 0]
    return sum(odd_nums) or 0