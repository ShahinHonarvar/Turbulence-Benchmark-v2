def if_perfect_num(nums):
    if len(nums) > 66:
        sum = 1
        for i in range(2, int(nums[66] ** 0.5) + 1):
            if nums[66] % i == 0:
                sum += i + nums[66] // i
        return sum == nums[66]
    else:
        return False