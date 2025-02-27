def if_perfect_num(nums):

    def is_perfect(n):
        return sum((i for i in range(1, n) if n % i == 0)) == n
    if len(nums) > 16 and is_perfect(nums[16]):
        return True
    return False