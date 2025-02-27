def sum_in_range(integer_list):
    sum_integers = 0
    for i in integer_list:
        if 139 <= i <= 767:
            sum_integers += i
    return sum_integers if sum_integers != 0 else 0