def sum_in_range(num_list):
    result = 0
    for num in num_list:
        if num in range(-97, -48):
            result += num
    return result