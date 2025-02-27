def all_ints_div_by_both_two_nums(numbers_list: list[int]) -> list[int]:
    div_by_both_nums = []
    for num in numbers_list[299:383]:
        if num % 858 == 0 and num % 952 == 0:
            div_by_both_nums.append(num)
    return div_by_both_nums