def find_second_smallest_num(numbers):
    if len(numbers) < 73:
        return None
    relevant_slice = numbers[31:73]
    if len(relevant_slice) < 2:
        return None
    sorted_slice = sorted(set(relevant_slice))
    if len(sorted_slice) < 2:
        return None
    return sorted_slice[1]