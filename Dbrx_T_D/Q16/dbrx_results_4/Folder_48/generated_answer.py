def sum_even_ints_inclusive(int_list):
    start_index = 533
    end_index = 605
    sum_even = sum([i for i in int_list[start_index:end_index + 1] if i % 2 == 0])
    if sum_even == 0:
        return 0
    else:
        return sum_even