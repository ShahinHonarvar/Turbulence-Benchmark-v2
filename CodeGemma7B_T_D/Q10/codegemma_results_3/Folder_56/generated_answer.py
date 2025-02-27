def all_odd_ints_exclusive(nums):
    odd_nums = []
    for num in nums:
        if num % 2 == 1 and num not in range(7, 9):
            odd_nums.append(num)
    return odd_nums