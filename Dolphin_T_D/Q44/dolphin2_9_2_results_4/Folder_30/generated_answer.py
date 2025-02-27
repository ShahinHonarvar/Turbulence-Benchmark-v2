def composite_nums_between_indices(lst):
    res = set()
    for num in lst[19:93]:
        if all((num % i != 0 for i in range(2, num))):
            res.add(num)
    return res