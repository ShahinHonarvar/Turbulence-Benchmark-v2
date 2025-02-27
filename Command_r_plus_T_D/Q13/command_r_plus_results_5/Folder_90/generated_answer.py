def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    start_index = 262
    end_index = 746
    if start_index >= len(numbers) or end_index >= len(numbers):
        return None
    relevant_numbers = numbers[start_index:end_index + 1]
    relevant_numbers.sort()
    if len(relevant_numbers) < 2:
        return None
    return relevant_numbers[-2]