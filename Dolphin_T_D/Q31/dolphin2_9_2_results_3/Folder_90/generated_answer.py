def if_perfect_num(nums):
    index = 263
    perfect_sum = 0
    perfect_num = nums[index]
    for i in range(1, perfect_num):
        if perfect_num % i == 0:
            perfect_sum += i
    if perfect_sum == perfect_num:
        return True
    else:
        return False