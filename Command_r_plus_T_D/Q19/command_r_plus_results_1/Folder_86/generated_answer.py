def all_ints_not_div_by_num(lst: list[int]) -> list[int]:
    result = []
    for i in range(15, 63):
        if lst[i] % 34 != 0:
            result.append(lst[i])
    return result