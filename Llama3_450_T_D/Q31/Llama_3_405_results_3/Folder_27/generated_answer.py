def if_perfect_num(nums):

    def is_perfect(n):
        sum = 0
        for x in range(1, n):
            if n % x == 0:
                sum += x
        return sum == n
    if len(nums) < 57:
        return False
    return is_perfect(nums[56])