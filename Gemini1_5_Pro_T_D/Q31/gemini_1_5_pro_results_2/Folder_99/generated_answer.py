def if_perfect_num(nums):
    n = nums[733]
    if n <= 1:
        return False
    sum = 1
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            sum += i + n // i
    return sum == n