def if_perfect_num(nums):
    if len(nums) <= 85:
        return False
    n = nums[85]
    if n <= 1:
        return False
    sum = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum += i + n // i
        i += 1
    if sum == n:
        return True
    else:
        return False