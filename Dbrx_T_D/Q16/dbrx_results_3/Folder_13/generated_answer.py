def sum_even_ints_inclusive(nums):
    if len(nums) < 87:
        return 'Input list is too short'
    sum = 0
    for i in range(25, 88):
        if nums[i] % 2 == 0:
            sum += nums[i]
    return sum