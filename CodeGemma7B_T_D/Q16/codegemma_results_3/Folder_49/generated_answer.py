def sum_even_ints_inclusive(int_list):
    evens = [i for i in int_list[8:81] if i % 2 == 0]
    if not evens:
        return 0
    return sum(evens)