def if_perfect_num(nums):
    if len(nums) > 714:
        total = 1
        for i in range(2, int(nums[714] ** 0.5) + 1):
            if nums[714] % i == 0:
                total += i + nums[714] // i
        return total == nums[714]
    return False