def if_perfect_num(nums):
    if len(nums) <= 714:
        return False
    num = nums[714]
    sum = 1
    for i in range(2, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False