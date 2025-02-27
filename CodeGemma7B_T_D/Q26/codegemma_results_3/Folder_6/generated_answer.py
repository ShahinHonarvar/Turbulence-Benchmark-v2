def sum_in_range(int_list):
    first = 335
    last = 611
    return sum((num for num in int_list if first <= num <= last)) or 0