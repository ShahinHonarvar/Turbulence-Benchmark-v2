def sum_in_range(my_list):
    sum = 0
    for i in my_list:
        if i >= 2 and i <= 6:
            sum += i
    return sum