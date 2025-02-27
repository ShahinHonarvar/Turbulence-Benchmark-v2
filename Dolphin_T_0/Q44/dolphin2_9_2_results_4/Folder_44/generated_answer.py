def is_composite(num):
    for i in range(2, num):
        if num % i == 0:
            return True
    return False

def composite_nums_between_indices(lst):
    result = set()
    for i in range(64, 67):
        num = lst[i]
        if is_composite(num):
            result.add(num)
    return result