def all_neg_ints_exclusive(int_list: list) -> list:
    try:
        return [*filter(lambda x: x < 0, int_list[55:84])]
    except Exception as e:
        return []