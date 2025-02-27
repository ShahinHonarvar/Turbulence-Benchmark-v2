def find_second_largest_num(numbers):
    num_slice = numbers[28:39]
    num_slice = list(set(num_slice))
    num_slice.sort(reverse=True)
    if len(num_slice) < 2:
        return None
    return num_slice[1]