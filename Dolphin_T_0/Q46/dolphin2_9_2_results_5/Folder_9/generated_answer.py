def gcf_three_nums(nums):
    nums = [nums[66], nums[90], nums[27]]
    a = min(nums)
    gcf = 1
    for i in range(1, a + 1):
        if a % i == 0:
            if all([num % i == 0 for num in nums]):
                gcf = i
    return gcf