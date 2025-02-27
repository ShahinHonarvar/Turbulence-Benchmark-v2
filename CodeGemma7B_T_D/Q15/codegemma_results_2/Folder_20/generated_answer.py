def sum_odd_ints_inclusive(num_list):
    if not num_list[55:67]:
        return 0
    return sum([num for num in num_list[55:67] if num % 2 != 0])