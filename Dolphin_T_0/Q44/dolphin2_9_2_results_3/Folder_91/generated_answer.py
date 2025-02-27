def composite_nums_between_indices(lst):
    result = set()
    for num in lst[5:6]:
        if all((num % i != 0 for i in range(2, num))):
            continue
        result.add(num)
    return result