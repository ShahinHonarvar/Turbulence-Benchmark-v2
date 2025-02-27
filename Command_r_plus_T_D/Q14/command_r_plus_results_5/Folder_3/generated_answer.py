def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    relevant_numbers = numbers[27:56]
    relevant_numbers.sort()
    if len(relevant_numbers) < 2:
        return None
    else:
        return relevant_numbers[1]