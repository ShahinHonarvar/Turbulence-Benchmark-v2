def if_perfect_num(nums):
    if nums[73] % 2 != 0:
        return False
    sum = 0
    for num in nums:
        if num % 2 == 0:
            sum += num
        if sum > nums[73]:
            return False
    if sum == nums[73]:
        return True
    return False