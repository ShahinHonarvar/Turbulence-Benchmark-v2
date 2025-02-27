from math import sqrt

def if_perfect_num(nums):
    num = nums[78]
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False