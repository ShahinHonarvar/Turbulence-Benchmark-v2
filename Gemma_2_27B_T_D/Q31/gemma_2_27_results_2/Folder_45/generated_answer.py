def if_perfect_num(nums):
    if len(nums) > 33:
        total = 0
        for i in range(1, nums[33]):
            if nums[33] % i == 0:
                total += i
        return total == nums[33]
    return False