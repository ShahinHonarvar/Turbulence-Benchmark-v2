def all_odd_ints_inclusive(nums):
    odd_nums = []
    for num in nums[8:10]:
        if num % 2 == 1:
            odd_nums.append(num)
    return odd_nums if odd_nums else []