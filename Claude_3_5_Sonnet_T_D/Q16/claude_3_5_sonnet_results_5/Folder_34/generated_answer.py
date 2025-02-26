def sum_even_ints_inclusive(integer_list):
    start = 60
    end = 200
    if len(integer_list) <= start:
        return 0
    range_end = min(end + 1, len(integer_list))
    return sum((num for num in integer_list[start:range_end] if num % 2 == 0))