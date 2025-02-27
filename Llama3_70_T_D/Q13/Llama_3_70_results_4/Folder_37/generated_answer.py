def find_second_largest_num(numbers):
    num_slice = numbers[1:6]
    if len(num_slice) < 2:
        return None
    num_slice.sort(reverse=True)
    return num_slice[1]