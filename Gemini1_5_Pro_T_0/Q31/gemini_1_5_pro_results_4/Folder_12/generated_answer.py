def if_perfect_num(nums):
    if len(nums) <= 27:
        return False
    num = nums[27]
    if num <= 1:
        return False
    sum = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            sum += i + num // i
        i += 1
    if sum == num:
        return True
    else:
        return False