def all_ints_div_by_num(numbers_list: list[int]) -> list[int]:
    divisible_by_57 = []
    for index, num in enumerate(numbers_list[22:24], start=23):
        if num % -57 == 0:
            divisible_by_57.append(num)
    return divisible_by_57