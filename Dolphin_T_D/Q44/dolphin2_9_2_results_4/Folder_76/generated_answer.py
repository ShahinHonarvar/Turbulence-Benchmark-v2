def is_composite(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return True
    return False

def composite_nums_between_indices(lst):
    return set((n for n in lst[639:976] if is_composite(n)))