def if_perfect_num(nums):
    for n in range(len(nums)):
        sum_num = 0
        for i in range(1, n):
            if n % i == 0:
                sum_num += i
        if sum_num == nums[n]:
            return True
    return False