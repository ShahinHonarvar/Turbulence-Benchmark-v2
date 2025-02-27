def find_second_smallest_num(numbers):
    num_slice = sorted(numbers[82:87])
    return num_slice[1] if len(num_slice) > 1 else None