def if_perfect_num(nums):
    return nums[263] % perfect_num(nums[263]) == 0

def perfect_num(x):
    sum = 0
    for i in range(1, x):
        if x % i == 0:
            sum += i
    return sum == x