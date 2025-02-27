def if_perfect_num(nums):
    if len(nums) > 66:
        total = 1
        for i in range(2, int(nums[66] ** 0.5) + 1):
            if nums[66] % i == 0:
                total += i + nums[66] // i
        return total == nums[66]
    return False