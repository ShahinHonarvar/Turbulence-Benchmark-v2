def sum_in_range(num_list):
    result = 0
    for num in num_list:
        if 60 <= num <= 90:
            result += num
    return result