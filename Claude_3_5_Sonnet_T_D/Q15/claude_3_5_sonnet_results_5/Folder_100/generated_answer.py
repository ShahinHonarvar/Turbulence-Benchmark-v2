def sum_odd_ints_inclusive(integers):
    start = 42
    end = 69
    if len(integers) <= start:
        return 0
    relevant_range = integers[start:end]
    odd_numbers = [num for num in relevant_range if num % 2 != 0]
    return sum(odd_numbers)