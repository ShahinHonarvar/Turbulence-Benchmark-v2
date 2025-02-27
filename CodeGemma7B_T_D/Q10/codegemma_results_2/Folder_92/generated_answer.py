def all_odd_ints_exclusive(nums):
    odd_nums = []
    for num in nums:
        if num % 2 != 0 and num > -1 and (num < 2):
            odd_nums.append(num)
    return odd_nums