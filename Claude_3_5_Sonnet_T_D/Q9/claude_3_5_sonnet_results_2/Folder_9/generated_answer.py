def all_odd_ints_inclusive(integer_list):
    start = 70
    end = 201
    return [num for num in integer_list[start:end] if num % 2 != 0]