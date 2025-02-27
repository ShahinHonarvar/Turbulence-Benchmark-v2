def if_perfect_num(nums):
    if len(nums) <= 990:
        return False
    sum = 1
    for i in range(2, int(nums[990] ** 0.5) + 1):
        if nums[990] % i == 0:
            sum += i + nums[990] // i
    if sum == nums[990]:
        return True
    else:
        return False