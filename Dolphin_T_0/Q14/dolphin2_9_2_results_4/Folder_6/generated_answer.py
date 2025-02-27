def find_second_smallest_num(numbers):
    slice_numbers = numbers[29:80]
    if len(slice_numbers) == 0:
        return None
    distinct_numbers = list(set(slice_numbers))
    distinct_numbers.sort()
    if len(distinct_numbers) < 2:
        return None
    else:
        return distinct_numbers[1]