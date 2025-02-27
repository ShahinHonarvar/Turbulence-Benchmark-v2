def if_perfect_num(nums):

    def is_perfect(n):
        if n < 1:
            return False
        return sum((i for i in range(1, n) if n % i == 0)) == n
    if len(nums) > 60:
        return is_perfect(nums[60])
    return False