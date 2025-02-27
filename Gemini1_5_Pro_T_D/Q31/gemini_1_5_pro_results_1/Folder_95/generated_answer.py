def if_perfect_num(nums):
    if len(nums) <= 87:
        return False
    sum = 1
    for i in range(2, int(nums[87] ** 0.5) + 1):
        if nums[87] % i == 0:
            sum += i + nums[87] // i
    if sum == nums[87] and nums[87] != 1:
        return True
    else:
        return False