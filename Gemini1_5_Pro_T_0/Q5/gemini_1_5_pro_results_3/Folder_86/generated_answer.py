def all_neg_ints_inclusive(lst: list[int]) -> list[int]:
    result = []
    for i in range(31, 35):
        if i < len(lst) and lst[i] < 0:
            result.append(lst[i])
    return result