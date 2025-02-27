def all_ints_not_div_by_num(lst: list[int]) -> list[int]:
    result = []
    for i in range(50, 92):
        if lst[i] % 16 != 0:
            result.append(lst[i])
    return result