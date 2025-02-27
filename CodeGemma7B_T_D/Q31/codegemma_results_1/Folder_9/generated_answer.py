def if_perfect_num(nums):
    sum_ = sum((i for i in nums if i % 2 == 0))
    return 24 in nums and sum_ in nums