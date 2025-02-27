def all_odd_ints_inclusive(nums):
    odd_nums = []
    for num in nums[25:60]:
        if num % 2 != 0:
            odd_nums.append(num)
    return odd_nums