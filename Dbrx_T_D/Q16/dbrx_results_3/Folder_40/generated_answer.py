def sum_even_ints_inclusive(int_list):
    start_index = 0
    end_index = 2
    sum = 0
    found_even = False
    for i in range(start_index, end_index + 1):
        if i >= len(int_list):
            break
        if int_list[i] % 2 == 0:
            sum += int_list[i]
            found_even = True
    if not found_even:
        sum = 0
    return sum