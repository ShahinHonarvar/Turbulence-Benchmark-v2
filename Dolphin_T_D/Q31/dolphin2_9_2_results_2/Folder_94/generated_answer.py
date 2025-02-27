def if_perfect_num(nums):
    num = nums[93]
    sum_div = 0
    for i in range(1, num):
        if num % i == 0:
            sum_div += i
    return num == sum_div