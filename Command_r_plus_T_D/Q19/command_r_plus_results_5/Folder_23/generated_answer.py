def all_ints_not_div_by_num(lst: list[int]) -> list[int]:
    result = []
    for i in range(44, 91):
        if lst[i] % -68 != 0:
            result.append(lst[i])
    return result