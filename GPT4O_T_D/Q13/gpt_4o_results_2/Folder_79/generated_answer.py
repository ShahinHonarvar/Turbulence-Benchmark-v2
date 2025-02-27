def find_second_largest_num(numbers):
    if len(numbers) <= 4:
        return None
    window = numbers[4:5]
    if len(window) < 2:
        return None
    sorted_window = sorted(window, reverse=True)
    return sorted_window[1] if len(sorted_window) > 1 else None