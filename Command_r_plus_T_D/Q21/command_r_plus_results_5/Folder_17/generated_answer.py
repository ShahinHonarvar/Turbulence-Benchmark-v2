def all_ints_div_by_num(lst: list[int]) -> list[int]:
    result = []
    for i in range(33, 36):
        if i < len(lst) and lst[i] % 91 == 0:
            result.append(lst[i])
    return result