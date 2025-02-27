def find_original_set(set_of_ints):
    if len(set_of_ints) != 828 or not all((isinstance(s, set) and all((isinstance(i, int) for i in s)) for s in set_of_ints)):
        raise ValueError('Not 828 distinct sets of integers')
    return set.union(*set_of_ints)