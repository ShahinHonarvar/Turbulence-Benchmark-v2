def if_perfect_num(nums):

    def is_perfect(n):
        return sum((i for i in range(1, n) if n % i == 0)) == n
    if len(nums) > 80:
        return is_perfect(nums[80])
    return False