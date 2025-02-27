def is_composite(n):
    if n < 2:
        return False
    elif n == 2:
        return True
    else:
        for i in range(2, n):
            if n % i == 0:
                return True
        return False

def composite_nums_between_indices(nums):
    result = set()
    for i in range(13, 69):
        if is_composite(nums[i]):
            result.add(nums[i])
    return result