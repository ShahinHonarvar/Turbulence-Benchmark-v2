def is_composite(num):
    if num < 4:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    if len(lst) < 10:
        return set()
    return {num for num in lst[8:10] if is_composite(num)}