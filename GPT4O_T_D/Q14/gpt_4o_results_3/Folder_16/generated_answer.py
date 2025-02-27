def find_second_smallest_num(numbers):
    relevant_slice = numbers[66:78]
    if len(relevant_slice) < 2:
        return None
    sorted_slice = sorted(relevant_slice)
    return sorted_slice[1]