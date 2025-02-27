def find_second_smallest_num(numbers):
    num_slice = numbers[:8]
    if len(num_slice) < 2:
        return None
    num_slice.sort()
    return num_slice[1]