def if_perfect_num(nums):
    if nums[56] == perfect_num(nums[56]):
        return True
    else:
        return False

def perfect_num(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    if num == sum:
        return True
    else:
        return False