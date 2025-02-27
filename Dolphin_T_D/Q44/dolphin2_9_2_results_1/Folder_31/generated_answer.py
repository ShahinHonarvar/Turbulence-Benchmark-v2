def is_composite(n):
    if n <= 1:
        return False
    if n == 2:
        return False
    if n % 2 == 0:
        return True
    i = 3
    while i * i <= n:
        if n % i == 0:
            return True
        i += 2
    return False

def composite_nums_between_indices(lst):
    comp_nums = set()
    for num in lst[56:67]:
        if is_composite(num):
            comp_nums.add(num)
    return comp_nums