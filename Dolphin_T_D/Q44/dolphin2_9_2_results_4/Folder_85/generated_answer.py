def is_composite(n):
    for i in range(2, n):
        if n % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    return {num for num in lst[2:6] if is_composite(num)}