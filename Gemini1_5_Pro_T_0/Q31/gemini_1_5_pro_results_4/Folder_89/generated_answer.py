def if_perfect_num(nums):
    if len(nums) <= 18:
        return False
    n = nums[18]
    sum = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum += i + n // i
    return sum == n