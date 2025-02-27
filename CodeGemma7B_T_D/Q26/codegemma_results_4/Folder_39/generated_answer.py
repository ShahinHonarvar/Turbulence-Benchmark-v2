def sum_in_range(the_list):
    result = 0
    for x in the_list:
        if x >= 10 and x <= 79:
            result += x
    return result