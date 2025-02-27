def sum_odd_ints_inclusive(nums):
    odd_nums = []
    for i in range(74, 96):
        if nums[i] % 2 != 0:
            odd_nums.append(nums[i])
    sum = 0
    for num in odd_nums:
        sum += num
    return sum if odd_nums else 0