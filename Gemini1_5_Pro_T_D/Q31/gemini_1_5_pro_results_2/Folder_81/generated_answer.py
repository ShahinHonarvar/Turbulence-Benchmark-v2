def if_perfect_num(nums):
    if len(nums) <= 20:
        return False
    num = nums[20]
    if num <= 1:
        return False
    divisors = []
    for i in range(1, num):
        if num % i == 0:
            divisors.append(i)
    sum_of_divisors = sum(divisors)
    if sum_of_divisors == num:
        return True
    else:
        return False