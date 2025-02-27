def if_perfect_num(nums):
    n = nums[828]
    sum_div = sum([i for i in range(1, n) if n % i == 0])
    return sum_div == n