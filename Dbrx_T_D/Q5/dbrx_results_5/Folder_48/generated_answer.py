def all_neg_ints_inclusive(my_list):
    start = 533
    end = 605
    if end >= len(my_list):
        return []
    return [i for i in my_list[start:end + 1] if i < 0]