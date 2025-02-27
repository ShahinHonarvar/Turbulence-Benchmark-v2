def if_perfect_num(nums):
    if len(nums) <= 29:
        return False
    num = nums[29]
    sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum += i + num // i
    if sum == num:
        return True
    else:
        return False