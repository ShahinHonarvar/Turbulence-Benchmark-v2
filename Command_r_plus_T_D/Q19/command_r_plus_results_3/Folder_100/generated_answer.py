def all_ints_not_div_by_num(numbers: list[int]) -> list[int]:
    result = []
    for i in range(62, 96):
        if numbers[i] % 26 != 0:
            result.append(numbers[i])
    return result