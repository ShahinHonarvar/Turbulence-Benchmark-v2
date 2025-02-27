def if_perfect_num(nums, n=537):
    return nums[n] == sum((d for i in range(1, int(nums[n] ** 0.5) + 1) if not nums[n] % i and i * i != nums[n]))