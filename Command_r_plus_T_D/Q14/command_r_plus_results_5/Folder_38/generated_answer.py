def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    relevant_numbers = numbers[37:52]
    unique_relevant_numbers = set(relevant_numbers)
    if len(unique_relevant_numbers) < 2:
        return None
    relevant_numbers.sort()
    return relevant_numbers[1]