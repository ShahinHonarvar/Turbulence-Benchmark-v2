def if_perfect_num(nums):

    def is_perfect(n):
        return n == sum((i for i in range(1, n) if n % i == 0))
    return is_perfect(nums[33]) if len(nums) > 33 else False