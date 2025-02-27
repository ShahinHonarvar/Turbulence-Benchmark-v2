def if_perfect_num(nums):
    n = nums[459]
    sum = 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            sum = sum + i + n / i
        i += 1
    return sum == n