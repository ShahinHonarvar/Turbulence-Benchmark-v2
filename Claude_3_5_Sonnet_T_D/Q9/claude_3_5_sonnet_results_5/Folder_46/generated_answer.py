def all_odd_ints_inclusive(integers):
    start_index = 30
    end_index = 88
    return [num for num in integers[start_index:end_index] if num % 2 != 0]