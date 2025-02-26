def find_second_largest_num(numbers):
    relevant_slice = numbers[40:81]
    if len(relevant_slice) < 2:
        return None
    sorted_slice = sorted(relevant_slice, reverse=True)
    return sorted_slice[1]