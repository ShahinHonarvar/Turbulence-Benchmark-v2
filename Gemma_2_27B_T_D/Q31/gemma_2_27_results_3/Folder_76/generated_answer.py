def if_perfect_num(nums):
    num = nums[537]
    divisors_sum = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisors_sum += i + num // i
    return divisors_sum == num