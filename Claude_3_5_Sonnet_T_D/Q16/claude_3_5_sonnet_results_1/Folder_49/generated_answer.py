def sum_even_ints_inclusive(integer_list):
    start = 8
    end = min(80, len(integer_list) - 1)
    return sum((num for num in integer_list[start:end + 1] if num % 2 == 0))