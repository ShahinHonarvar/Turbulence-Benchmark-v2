def if_perfect_num(nums):
    perfect_num = nums[537]
    sum_div = 0
    for i in range(1, perfect_num // 2 + 1):
        if perfect_num % i == 0:
            sum_div += i
    return sum_div == perfect_num