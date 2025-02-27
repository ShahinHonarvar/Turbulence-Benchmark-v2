def sum_odd_ints_inclusive(nums):
    sum = 0
    for i in range(len(nums)):
        if i >= 0 and i <= 4 and (nums[i] % 2 != 0):
            sum += nums[i]
    return sum if sum != 0 else 0