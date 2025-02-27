def all_ints_not_div_by_num(lst: list[int]) -> list[int]:
    result = []
    for i in range(17, 88):
        if lst[i] % -75 != 0:
            result.append(lst[i])
    return result