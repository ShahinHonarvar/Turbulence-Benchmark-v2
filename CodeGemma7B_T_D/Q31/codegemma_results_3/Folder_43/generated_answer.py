def if_perfect_num(nums):
    return nums[29] if perfect_num(nums[29]) else False

def perfect_num(n):
    return sum((i for i in range(1, n) if n % i == 0)) == n