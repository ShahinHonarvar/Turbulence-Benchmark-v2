def all_ints_div_by_num(lst: list[int]) -> list[int]:
    result = []
    for i in range(29, 52):
        if lst[i] % -37 == 0:
            result.append(lst[i])
    return result