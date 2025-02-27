def if_perfect_num(nums):
    if len(nums) < 101:
        return False
    num = nums[100]
    sum = 1
    for i in range(2, num):
        if num % i == 0:
            sum += i
    return sum == num