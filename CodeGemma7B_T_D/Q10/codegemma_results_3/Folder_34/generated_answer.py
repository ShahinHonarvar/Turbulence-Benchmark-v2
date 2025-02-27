def all_odd_ints_exclusive(nums):
    odd_nums = []
    for num in nums[60:200]:
        if num % 2 != 0:
            odd_nums.append(num)
    return odd_nums if odd_nums else []