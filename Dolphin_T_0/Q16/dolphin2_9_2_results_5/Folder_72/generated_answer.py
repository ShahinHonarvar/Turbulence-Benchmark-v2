def sum_even_ints_inclusive(int_list):
    sum_of_evens = 0
    for num in int_list[29:52]:
        if num % 2 == 0:
            sum_of_evens += num
    return sum_of_evens