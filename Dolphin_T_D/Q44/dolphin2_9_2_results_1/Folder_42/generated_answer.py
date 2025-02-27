def composite_nums_between_indices(lst):
    result = set()
    for i in range(91, 100):
        number = lst[i]
        if all((number % i != 0 for i in range(2, int(number ** 0.5) + 1))):
            result.add(number)
    return result