def sum_even_ints_inclusive(integer_list):
    start = 10
    end = min(100, len(integer_list) - 1)
    return sum((num for num in integer_list[start:end + 1] if num % 2 == 0))