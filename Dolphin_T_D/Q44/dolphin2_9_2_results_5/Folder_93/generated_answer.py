def is_composite(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    output_set = set()
    for i in range(23, 24):
        if is_composite(lst[i]):
            output_set.add(lst[i])
    return output_set