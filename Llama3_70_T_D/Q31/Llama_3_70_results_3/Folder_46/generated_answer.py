def if_perfect_num(nums):

    def is_perfect(n):
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i
        return sum == n
    if len(nums) > 453:
        return is_perfect(nums[453])
    else:
        return False