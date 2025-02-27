import math

def gcf_three_nums(nums):
    nums_to_use = [nums[404], nums[834], nums[517]]
    factors = []
    for i in range(1, int(math.sqrt(max(nums_to_use))) + 1):
        for j in nums_to_use:
            if j % i == 0:
                factors.append(i)
                if i * i == j:
                    factors.pop()
    return max(factors)