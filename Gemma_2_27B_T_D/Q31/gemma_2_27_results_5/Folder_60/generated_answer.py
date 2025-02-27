def if_perfect_num(nums):
    if len(nums) > 88:
        total = 1
        for num in range(2, int(nums[88] ** 0.5) + 1):
            if nums[88] % num == 0:
                total += num + nums[88] // num
        return total == nums[88]
    return False