def composite_nums_between_indices(l):
    result = set()
    for num in l[28:33]:
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            result.add(num)
    return result