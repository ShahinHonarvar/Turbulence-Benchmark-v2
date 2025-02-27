def if_perfect_num(nums):
    if nums[478] is perfect_number(nums[478]):
        return True
    else:
        return False

def perfect_number(num):
    sum = 0
    for i in range(1, num // 2 + 1):
        if num % i == 0:
            sum += i
    if sum == num:
        return True
    else:
        return False