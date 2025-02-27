def if_perfect_num(nums):
    if nums[53] % 2 == 1:
        return False
    num = nums[53]
    sum = num + 1
    while num != sum >> 1:
        num, sum = (sum, num + sum)
    if sum == nums[53] + nums[53]:
        return True
    return False