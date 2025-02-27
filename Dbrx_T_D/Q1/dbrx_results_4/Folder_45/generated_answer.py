def all_ints_inclusive(list_of_ints):
    if len(list_of_ints) >= 200 and 30 in range(len(list_of_ints)):
        return list_of_ints[30:201]
    else:
        raise IndexError('List is not long enough')