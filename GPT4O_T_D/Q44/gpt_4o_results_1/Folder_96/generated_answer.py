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
    composite_set = set()
    for i in range(60, min(201, len(nums))):
        if is_composite(nums[i]):
            composite_set.add(nums[i])
    return composite_set