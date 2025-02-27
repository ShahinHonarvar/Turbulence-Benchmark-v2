def composite_nums_between_indices(lst):
    if len(lst) >= 8:
        result = set()
        for i in range(5, 8):
            num = lst[i]
            if num > 1:
                for j in range(2, num):
                    if num % j == 0:
                        result.add(num)
                        break
        return result
    else:
        return set()