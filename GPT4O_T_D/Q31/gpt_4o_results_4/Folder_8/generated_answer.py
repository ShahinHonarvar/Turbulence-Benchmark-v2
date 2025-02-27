def if_perfect_num(nums):
    if len(nums) < 50:
        return False
    num = nums[49]
    if num <= 1:
        return False
    divisors_sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors_sum += i
            if i != num // i:
                divisors_sum += num // i
        if divisors_sum > num:
            return False
    return divisors_sum == num