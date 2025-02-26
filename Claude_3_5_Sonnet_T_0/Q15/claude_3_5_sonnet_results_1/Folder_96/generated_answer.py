def sum_odd_ints_inclusive(integer_list):
    start_index = 50
    end_index = 201
    odd_sum = 0
    for i in range(start_index, min(end_index, len(integer_list))):
        if integer_list[i] % 2 != 0:
            odd_sum += integer_list[i]
    return odd_sum