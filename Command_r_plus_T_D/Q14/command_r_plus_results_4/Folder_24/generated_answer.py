def find_second_smallest_num(numbers: list[int]) -> int:
    if len(numbers) < 23:
        return None
    else:
        sorted_numbers = sorted(numbers[23:24])
        if len(sorted_numbers) < 2:
            return None
        else:
            return sorted_numbers[1]