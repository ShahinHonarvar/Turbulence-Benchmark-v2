def sum_in_range(my_list):
    result = 0
    for integer in my_list:
        if -23 <= integer <= 64:
            result += integer
    return result