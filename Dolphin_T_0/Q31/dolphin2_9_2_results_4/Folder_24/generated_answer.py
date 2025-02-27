def if_perfect_num(nums):

    def is_perfect(n):
        return sum((x for x in range(1, n) if n % x == 0)) == n
    return is_perfect(nums[74])