def if_perfect_num(nums):
    if nums[685] < 0:
        return False
    sum = 0
    for i in range(1, nums[685]):
        if nums[685] % i == 0:
            sum += i
    return nums[685] == sum