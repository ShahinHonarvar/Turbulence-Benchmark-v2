def composite_nums_between_indices(lst):
    result = set()
    for num in lst[262:747]:
        if num > 1 and (num % 2 == 0 or num % 3 == 0):
            result.add(num)
    return result