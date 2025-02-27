def sum_odd_ints_inclusive(nums):
    if not nums:
        return 0
    sum_odd = 0
    count = 0
    for i in range(68, 87):
        if i % 2 != 0:
            sum_odd += nums[i]
            count += 1
    if count == 0:
        return 0
    return sum_odd