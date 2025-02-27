def all_neg_ints_exclusive(integer_list):
    try:
        return [i for i in integer_list[5:9] if i < 0 and type(i) is int]
    except IndexError:
        return []
    except TypeError:
        return []