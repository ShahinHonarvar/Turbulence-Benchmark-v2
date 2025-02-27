from math import sqrt

def composite_nums_between_indices(nums):
    composites = {num for num in nums if num != 1 and int(sqrt(num)) > 1 and (num % int(sqrt(num)) == 0)}
    return composites