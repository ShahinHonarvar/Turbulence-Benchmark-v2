def is_composite(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    composites = set()
    for i in range(len(lst)):
        if is_composite(lst[i]) and i >= 0 and (i <= 2):
            composites.add(lst[i])
    return composites