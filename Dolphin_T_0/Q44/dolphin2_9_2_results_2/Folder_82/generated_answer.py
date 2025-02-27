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

def composite_nums_between_indices(lst):
    composite_nums = set()
    indices = range(30, 31)
    for num in lst:
        if num in indices:
            if is_composite(num):
                composite_nums.add(num)
    return composite_nums