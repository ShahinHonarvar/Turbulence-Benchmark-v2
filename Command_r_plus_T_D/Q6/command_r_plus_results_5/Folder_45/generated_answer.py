def all_neg_ints_exclusive(numbers_list: list[int]) -> list[int]:
    neg_numbers = [num for num in numbers_list[30:200] if num < 0]
    return neg_numbers