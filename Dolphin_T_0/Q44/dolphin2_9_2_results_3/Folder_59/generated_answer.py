def is_composite(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    return {lst[i] for i in range(len(lst)) if lst[i] > 0 and lst[i] < 10 and is_composite(lst[i])}