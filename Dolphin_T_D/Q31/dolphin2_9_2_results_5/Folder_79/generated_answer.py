def if_perfect_num(nums):
    if nums[63] < 0:
        return False
    else:
        sum = 1
        i = 2
        while i * i <= nums[63]:
            if nums[63] % i:
                i += 1
            elif i * (nums[63] // i) == nums[63]:
                sum = sum + i + nums[63] // i
                i += 1
            else:
                i += 1
        return sum == nums[63] and nums[63] != 1