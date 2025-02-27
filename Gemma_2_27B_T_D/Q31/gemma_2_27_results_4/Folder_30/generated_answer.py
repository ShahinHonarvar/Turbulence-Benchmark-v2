def if_perfect_num(nums):
    total = 1
    if nums[94] <= 1:
        return False
    for i in range(2, int(nums[94] ** 0.5) + 1):
        if nums[94] % i == 0:
            total += i + nums[94] // i
    if total == nums[94]:
        return True
    else:
        return False