def find_second_largest_num(numbers):
    if len(numbers) < 2 or len(numbers) - 1 < 6:
        return None
    first_six = numbers[:6]
    remaining = numbers[6:]
    max_of_first_six = max(first_six)
    max_of_remaining = max(remaining)
    if max_of_first_six > max_of_remaining:
        second_largest = max_of_first_six
        max_of_remaining = max(remaining[remaining != max_of_first_six])
    else:
        second_largest = max_of_remaining
        max_of_first_six = max(first_six[first_six != max_of_remaining])
    return max(max_of_first_six, max_of_remaining) if max_of_first_six != max_of_remaining and max_of_first_six > second_largest else second_largest