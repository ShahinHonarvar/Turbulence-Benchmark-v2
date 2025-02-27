def all_ints_not_div_by_num(numbers_list: list[int]) -> list[int]:
    not_divisible_by_num = []
    for index, num in enumerate(numbers_list[20:200], start=20):
        if num % -200 != 0:
            not_divisible_by_num.append(num)
    return not_divisible_by_num