def is_composite(n):
    if n <= 1:
        return False
    if n <= 3:
        return False
    if n % 2 == 0 or n % 3 == 0:
        return True
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return True
        i += 6
    return False

def composite_nums_between_indices(nums):
    composites = set()
    for i in range(21, min(98, len(nums))):
        if is_composite(nums[i]):
            composites.add(nums[i])
    return composites