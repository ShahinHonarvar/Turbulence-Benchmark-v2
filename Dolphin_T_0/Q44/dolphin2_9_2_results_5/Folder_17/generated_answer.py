def composite_nums_between_indices(lst):
    result = set()
    for i in range(50, 55):
        num = lst[i]
        if num > 1:
            for j in range(2, num):
                if num % j == 0:
                    result.add(num)
                    break
    return result