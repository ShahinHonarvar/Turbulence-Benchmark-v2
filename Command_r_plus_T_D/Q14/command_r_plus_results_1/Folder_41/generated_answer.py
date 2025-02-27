def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers) < 5:
        return None
    else:
        sorted_numbers = sorted(numbers[4:])
        return sorted_numbers[1] if len(sorted_numbers) > 1 else None