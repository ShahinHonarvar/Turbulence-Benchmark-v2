def find_second_largest_num(numbers):
    slice_numbers = numbers[75:86]
    if len(set(slice_numbers)) < 2:
        return None
    return sorted(set(slice_numbers), reverse=True)[1]