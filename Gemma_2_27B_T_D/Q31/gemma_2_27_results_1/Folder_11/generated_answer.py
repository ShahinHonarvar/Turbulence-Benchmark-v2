def if_perfect_num(nums):
    if len(nums) > 77:
        total = 1
        for i in range(2, int(nums[77] ** 0.5) + 1):
            if nums[77] % i == 0:
                total += i + nums[77] // i
        return total == nums[77]
    return False