def if_perfect_num(nums):

    def is_perfect(n):
        return n == sum((i for i in range(1, n) if n % i == 0))
    return len(nums) > 42 and is_perfect(nums[42])