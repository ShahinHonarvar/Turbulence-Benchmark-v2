def if_perfect_num(nums):
    num = nums[312]
    sum_of_factors = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_of_factors += i + num // i
    return sum_of_factors == num