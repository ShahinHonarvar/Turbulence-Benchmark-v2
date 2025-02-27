def all_neg_ints_inclusive(numbers_list):
    try:
        return [num for num in numbers_list[31:35] if num < 0]
    except IndexError:
        return []