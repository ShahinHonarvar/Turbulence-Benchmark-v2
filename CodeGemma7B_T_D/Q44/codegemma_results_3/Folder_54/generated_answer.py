def composite_nums_between_indices(nums):
    composites = set()
    for i in range(14, 65):
        if i in nums and is_composite(i):
            composites.add(i)
    return composites

def is_composite(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False