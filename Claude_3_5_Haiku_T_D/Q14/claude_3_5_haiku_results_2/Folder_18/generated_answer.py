def find_second_smallest_num(numbers):
    if len(numbers) < 49:
        return None
    slice_list = numbers[30:49]
    try:
        return sorted(set(slice_list))[1]
    except IndexError:
        return None