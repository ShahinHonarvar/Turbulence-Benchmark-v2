def sum_even_ints_inclusive(int_list):
    start_index = 111
    end_index = 111
    sum = 0
    for i in range(min(start_index, end_index), max(start_index, end_index) + 1):
        if i % 2 == 0 and i in int_list:
            sum += i
    return sum