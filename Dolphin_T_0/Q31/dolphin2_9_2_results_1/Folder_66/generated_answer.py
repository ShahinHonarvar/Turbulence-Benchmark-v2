def if_perfect_num(nums):
    num = nums[42]
    sum_div = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        elif i * (num // i) == num:
            sum_div = sum_div + i + num // i
            i += 1
        else:
            sum_div = sum_div + i
            i += 1
    return sum_div == num