def composite_nums_between_indices(lst):
    result = set()
    for i in range(70, 201):
        n = lst[i]
        if n > 1:
            for i in range(2, n):
                if n % i == 0:
                    result.add(n)
                    break
    return result