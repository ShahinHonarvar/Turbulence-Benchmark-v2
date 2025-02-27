def is_perfect_num(nums):
    num = nums[10]
    perfect = False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            perfect = True
            break
    return perfect