def all_ints_div_by_both_two_nums(int_list: list[int]) -> list[int]:
    divisible_by_both = []
    for index, num in enumerate(int_list[56:89], start=56):
        if num % -59 == 0 and num % -79 == 0:
            divisible_by_both.append(num)
    return divisible_by_both