def all_ints_not_div_by_num(lst: list[int]) -> list[int]:
    result = []
    for i in range(18, 60):
        if lst[i] % 86 != 0:
            result.append(lst[i])
    return result