def find_second_smallest_num(numbers):
    if len(numbers) < 69 or len(numbers[13:69]) < 2:
        return None
    sorted_subset = sorted(numbers[13:69])
    return sorted_subset[1]