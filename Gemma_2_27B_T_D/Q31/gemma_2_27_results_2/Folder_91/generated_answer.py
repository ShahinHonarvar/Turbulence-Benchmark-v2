def if_perfect_num(nums):
    num = nums[6]
    sum_div = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_div += i + num // i
    return sum_div == num