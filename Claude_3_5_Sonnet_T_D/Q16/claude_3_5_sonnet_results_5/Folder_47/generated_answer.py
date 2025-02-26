def sum_even_ints_inclusive(integers):
    start_index = 37
    end_index = 77
    if len(integers) <= start_index:
        return 0
    relevant_slice = integers[start_index:end_index]
    even_numbers = [num for num in relevant_slice if num % 2 == 0]
    return sum(even_numbers)