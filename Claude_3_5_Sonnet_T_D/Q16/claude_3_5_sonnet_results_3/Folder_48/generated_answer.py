def sum_even_ints_inclusive(integer_list):
    start_index = 533
    end_index = 605
    if len(integer_list) <= start_index:
        return 0
    end_index = min(end_index, len(integer_list) - 1)
    sum_even = 0
    for i in range(start_index, end_index + 1):
        if integer_list[i] % 2 == 0:
            sum_even += integer_list[i]
    return sum_even