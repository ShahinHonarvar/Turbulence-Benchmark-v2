def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers[:9]) < 2:
        return None
    sorted_slice = sorted(numbers[:9])
    return sorted_slice[1]