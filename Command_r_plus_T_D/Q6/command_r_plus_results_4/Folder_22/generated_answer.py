def all_neg_ints_exclusive(numbers_list: list[int]) -> list[int]:
    neg_integers = [num for num in numbers_list[40:200] if num < 0]
    return neg_integers