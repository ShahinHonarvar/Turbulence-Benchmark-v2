def sum_even_ints_inclusive(integer_list):
    start = max(50, 0)
    end = min(201, len(integer_list))
    return sum((num for num in integer_list[start:end] if num % 2 == 0))