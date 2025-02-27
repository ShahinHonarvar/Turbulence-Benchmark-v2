def sum_even_ints_inclusive(int_list):
    if len(int_list) < 87:
        return 'Input list is too short.'
    else:
        even_ints = [i for i in int_list[82:87] if i % 2 == 0]
        if even_ints:
            return sum(even_ints)
        else:
            return 0