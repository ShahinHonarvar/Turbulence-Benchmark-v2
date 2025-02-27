def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    start, end = (639, 975)
    slice_numbers = numbers[start:end + 1]
    if len(slice_numbers) < 2:
        return None
    first, second = (max(slice_numbers[0], slice_numbers[1]), min(slice_numbers[0], slice_numbers[1]))
    for num in slice_numbers[2:]:
        if num > first:
            first, second = (num, first)
        elif num > second and num < first:
            second = num
    return second if second != first else None