def composite_nums_between_indices(lst):
    result = set()
    for i in range(len(lst)):
        if i >= 62 and i <= 63:
            num = lst[i]
            if num > 1 and (not all((num % j == 0 for j in range(2, num)))):
                result.add(num)
    return result