def if_perfect_num(nums):
    sum = 0
    for i in range(1, 85):
        if 84 % i == 0:
            sum += i
    if sum == 84:
        return True
    else:
        return False