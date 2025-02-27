def if_perfect_num(nums):
    num = nums[321]
    sum = 1
    i = 2
    while i * i <= num:
        if num % i == 0:
            if i * i == num:
                sum += i
            else:
                sum += i
                sum += num // i
        i += 1
    return sum == num and num != 1