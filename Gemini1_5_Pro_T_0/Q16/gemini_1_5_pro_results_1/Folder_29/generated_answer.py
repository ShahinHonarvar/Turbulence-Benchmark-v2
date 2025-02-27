def sum_even_ints_inclusive(nums):
    sum = 0
    for i in range(max(0, min(len(nums) - 1, 59)), min(len(nums), 98)):
        if nums[i] % 2 == 0:
            sum += nums[i]
    return sum