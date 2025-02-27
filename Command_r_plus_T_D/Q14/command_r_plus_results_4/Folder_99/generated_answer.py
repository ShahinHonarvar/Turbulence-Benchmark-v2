def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers or len(numbers) < 609:
        return None
    sorted_window = sorted(numbers[608:609 + 1])
    if len(sorted_window) < 2:
        return None
    return sorted_window[1]