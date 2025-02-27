def all_odd_ints_exclusive(nums):
    odd_ints = []
    for num in nums[25:80]:
        if num % 2 != 0:
            odd_ints.append(num)
    return odd_ints