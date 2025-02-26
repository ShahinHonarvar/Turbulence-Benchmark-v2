def sum_even_ints_inclusive(integer_list):
    start_index = 25
    end_index = 60
    if len(integer_list) <= start_index:
        return 0
    relevant_slice = integer_list[start_index:end_index]
    even_numbers = [num for num in relevant_slice if num % 2 == 0]
    return sum(even_numbers)