from math import sqrt

def composite_nums_between_indices(nums):
    composites = set()
    for num in nums[37:52]:
        limit = int(sqrt(num)) + 1
        factor = 2
        while factor < limit:
            if num % factor == 0:
                composites.add(num)
                break
            factor += 1
    return composites