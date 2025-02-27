def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    sublist = numbers[25:60]
    unique_numbers = set(sublist)
    unique_numbers.discard(min(sublist))
    if len(unique_numbers) < 1:
        return None
    else:
        return min(unique_numbers)