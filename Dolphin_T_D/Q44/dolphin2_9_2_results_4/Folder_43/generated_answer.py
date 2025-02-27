def is_composite(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            return False
    return True

def composite_nums_between_indices(lst):
    composite_nums_lst = []
    for i in range(31, 73):
        if is_composite(lst[i]):
            composite_nums_lst.append(lst[i])
    return set(composite_nums_lst)