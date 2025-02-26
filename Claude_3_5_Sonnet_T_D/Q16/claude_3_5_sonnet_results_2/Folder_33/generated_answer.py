def sum_even_ints_inclusive(integers):
    start_index = 667
    end_index = 774
    return sum((num for num in integers[start_index:end_index + 1] if num % 2 == 0))