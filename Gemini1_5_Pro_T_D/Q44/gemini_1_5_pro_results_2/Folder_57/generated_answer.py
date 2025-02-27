def composite_nums_between_indices(lst):
    res = set()
    for i in range(max(25, 0), min(60, len(lst))):
        num = lst[i]
        if num > 1:
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    res.add(num)
                    break
    return res