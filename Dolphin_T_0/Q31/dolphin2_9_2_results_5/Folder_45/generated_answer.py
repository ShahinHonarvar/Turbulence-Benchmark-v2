def if_perfect_num(nums):

    def is_perfect(n):
        return sum((1 for i in range(1, n) if n % i == 0)) == n
    if 33 < len(nums):
        return is_perfect(nums[33])
    return False