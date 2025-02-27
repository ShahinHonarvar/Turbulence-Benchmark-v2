def composite_nums_between_indices(lst):
    result = set()
    for i in range(min(9, len(lst) - 1)):
        num = lst[i]
        if num > 1 and num < lst[9] and (not (num == 2 or num % 2 == 0)):
            for j in range(3, int(num ** 0.5) + 1, 2):
                if num % j == 0:
                    break
            else:
                result.add(num)
    return result