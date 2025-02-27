def is_composite(n):
    if n == 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    i = 3
    while i * i <= n:
        if n % i:
            i += 2
        else:
            return False
    return True

def composite_nums_between_indices(nums):
    composite_nums_between = set()
    for num in nums[661:925]:
        if is_composite(num):
            composite_nums_between.add(num)
    return composite_nums_between