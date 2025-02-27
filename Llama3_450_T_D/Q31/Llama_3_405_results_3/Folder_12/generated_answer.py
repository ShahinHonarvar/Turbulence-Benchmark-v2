def is_perfect(n):
    sum = 0
    for x in range(1, n):
        if n % x == 0:
            sum += x
    return sum == n

def if_perfect_num(nums):
    if len(nums) > 27:
        return is_perfect(nums[27])
    else:
        return False