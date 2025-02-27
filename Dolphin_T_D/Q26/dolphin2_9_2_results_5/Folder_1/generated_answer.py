def sum_in_range(int_list):
    sum = 0
    for i in int_list:
        if -97 <= i <= -48:
            sum += i
    return sum