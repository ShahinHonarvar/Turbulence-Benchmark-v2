def composite_nums_between_indices(lst):
    result = set()
    for i in range(62, 100):
        if is_composite(lst[i]):
            result.add(lst[i])
    return result

def is_composite(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return True
    return False