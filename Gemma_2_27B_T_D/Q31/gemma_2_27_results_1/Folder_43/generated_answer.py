def if_perfect_num(nums):
    num = nums[29]
    sum1 = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            sum1 = sum1 + i + num / i
        i += 1
    return sum1 == num