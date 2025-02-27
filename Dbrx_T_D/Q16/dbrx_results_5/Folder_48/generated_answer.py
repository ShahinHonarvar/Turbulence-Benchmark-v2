def sum_even_ints_inclusive(int_list):
    start_index = 533
    end_index = 605
    sum_of_evens = 0
    for i in range(min(start_index, end_index), max(start_index, end_index) + 1):
        current_int = int_list[i]
        if current_int % 2 == 0:
            sum_of_evens += current_int
    return sum_of_evens