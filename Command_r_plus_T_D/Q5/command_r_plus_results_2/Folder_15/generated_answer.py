def all_neg_ints_inclusive(numbers_list: list[int]) -> list[int]:
    neg_numbers = [num for num in numbers_list[:4] if num < 0]
    return neg_numbers