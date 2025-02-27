def is_composite(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    return {lst[i] for i in range(25, 60) if is_composite(lst[i])}