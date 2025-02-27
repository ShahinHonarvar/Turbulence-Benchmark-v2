def gcf_two_nums(nums):
    num1 = nums[841]
    num2 = nums[804]
    factors = []
    for i in range(1, max(num1, num2) + 1):
        if num1 % i == 0 and num2 % i == 0:
            factors.append(i)
    return max(factors)