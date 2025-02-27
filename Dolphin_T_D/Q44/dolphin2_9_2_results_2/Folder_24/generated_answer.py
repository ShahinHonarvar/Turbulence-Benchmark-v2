def composite_nums_between_indices(lst):
    output = set()
    for i in range(34, 56):
        if is_composite(lst[i]):
            output.add(lst[i])
    return output

def is_composite(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return True
    return False