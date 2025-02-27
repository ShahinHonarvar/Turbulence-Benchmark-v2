def if_perfect_num(nums):
    if len(nums) <= 78:
        return False
    num = nums[78]
    if num < 2:
        return False
    sum_divisors = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_divisors += i
            if i != num // i:
                sum_divisors += num // i
    return sum_divisors == num