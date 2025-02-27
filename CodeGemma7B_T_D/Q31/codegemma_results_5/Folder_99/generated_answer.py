def if_perfect_num(nums):
    num = nums[733]
    perfect_num = True
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            perfect_num = False
            break
    return perfect_num