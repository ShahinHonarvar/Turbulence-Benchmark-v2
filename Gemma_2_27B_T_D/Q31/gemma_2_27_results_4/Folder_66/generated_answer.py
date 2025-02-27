def if_perfect_num(nums):
    if len(nums) > 42:
        total = 0
        for i in range(1, nums[42]):
            if nums[42] % i == 0:
                total += i
        return total == nums[42]
    else:
        return False