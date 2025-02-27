def sum_in_range(num_list):
    temp_list = [num for num in num_list if -23 <= num <= 64]
    if not temp_list:
        return 0
    return sum(temp_list)