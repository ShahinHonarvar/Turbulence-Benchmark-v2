def all_odd_ints_exclusive(nums):
    odd_nums = []
    for num in nums[55:84]:
        if num % 2 != 0:
            odd_nums.append(num)
    return odd_nums