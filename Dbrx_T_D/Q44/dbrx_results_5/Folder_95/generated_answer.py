def composite_nums_between_indices(lst):
    if len(lst) < 53:
        return set()
    result = set()
    for i in range(26, 53):
        num = lst[i]
        if num > 1 and (not any((num % j == 0 for j in range(2, num)))):
            result.add(num)
    return result