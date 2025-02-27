def sum_in_range(int_list):
    sum = 0
    for i in int_list:
        if -100 <= i <= -55:
            sum += i
    return sum if sum != 0 else 0