def composite_nums_between_indices(lst):
    result = set()
    for i in range(22, 64):
        num = lst[i]
        if num > 1 and (not (num & 1 and num % 3 == 0)):
            for j in range(2, int(num ** 0.5) + 1):
                if num % j == 0:
                    break
            else:
                result.add(num)
    return result