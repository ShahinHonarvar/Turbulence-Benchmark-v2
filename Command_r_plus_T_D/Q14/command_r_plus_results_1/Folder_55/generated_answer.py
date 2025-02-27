def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers) < 11:
        return None
    else:
        sorted_numbers = sorted(numbers[10:11])
        return sorted_numbers[1] if len(sorted_numbers) > 1 else None