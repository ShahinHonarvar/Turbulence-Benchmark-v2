def sum_even_ints_inclusive(int_list):
    start_index = 50
    end_index = 200
    even_sum = 0
    for i in range(start_index, end_index + 1):
        if i >= len(int_list):
            break
        if int_list[i] % 2 == 0:
            even_sum += int_list[i]
    return even_sum if even_sum > 0 else 0