def sum_in_range(int_list):
    total_sum = 0
    for int in int_list:
        if -64 <= int <= 42:
            total_sum += int
    return total_sum