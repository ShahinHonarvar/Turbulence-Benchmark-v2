def if_perfect_num(nums):
    if nums[41] == 0:
        return False
    else:
        sum = 1
        i = 2
        while i * i <= nums[41]:
            if nums[41] % i:
                i += 1
            elif i * (nums[41] // i) == nums[41]:
                sum = sum + i + nums[41] // i
            else:
                sum = sum + i
            i += 1
        return sum == nums[41]