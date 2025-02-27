def find_second_smallest_num(numbers):
    slice_of_numbers = numbers[43:87]
    distinct_numbers = list(set(slice_of_numbers))
    distinct_numbers.sort()
    if len(distinct_numbers) < 2:
        return None
    return distinct_numbers[1]