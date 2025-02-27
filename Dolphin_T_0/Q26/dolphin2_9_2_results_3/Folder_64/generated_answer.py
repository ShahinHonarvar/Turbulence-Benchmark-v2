def sum_in_range(num_list):
    result = 0
    for i in num_list:
        if -3 <= i <= 6:
            result += i
    return result if result != 0 else 0