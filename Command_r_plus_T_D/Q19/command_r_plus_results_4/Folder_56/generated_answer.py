def all_ints_not_div_by_num(lst: list[int]) -> list[int]:
    result = []
    for i in range(7, 10):
        if i < len(lst) and lst[i] % -9 != 0:
            result.append(lst[i])
    return result