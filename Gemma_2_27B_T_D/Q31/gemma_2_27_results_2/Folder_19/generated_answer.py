def if_perfect_num(nums):
    if len(nums) > 13:
        total = 0
        for i in range(1, nums[13]):
            if nums[13] % i == 0:
                total += i
        return total == nums[13]
    else:
        return False