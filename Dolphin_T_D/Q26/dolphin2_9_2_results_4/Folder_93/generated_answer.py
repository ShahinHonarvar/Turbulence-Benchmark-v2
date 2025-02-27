def sum_in_range(list_of_ints):
    total = 0
    for i in list_of_ints:
        if -23 <= i <= 64:
            total += i
    return total