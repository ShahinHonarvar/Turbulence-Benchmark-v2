def gcf_two_nums(nums):
    if len(nums) != 2 or nums[360] <= 0 or nums[722] <= 0:
        raise ValueError('Invalid input: the list must have exactly two positive integers.')
    min_num = min(nums[360], nums[722])
    factors = set()
    for i in range(1, min_num + 1):
        if min_num % i == 0:
            factors.add(i)
    gcf = None
    for factor in factors:
        if factor in factors:
            gcf = factor
    return gcf