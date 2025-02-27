def is_composite(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    """Return set of composite numbers between the specified indices."""
    target_nums = lst[667:775]
    composite_nums = [num for num in target_nums if is_composite(num)]
    return set(composite_nums)