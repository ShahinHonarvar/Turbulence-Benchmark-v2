def find_second_smallest_num(numbers: list[int]) -> int:
    if not numbers or len(numbers) < 67:
        return None
    relevant_numbers = numbers[10:67]
    relevant_numbers.sort()
    if len(relevant_numbers) < 2:
        return None
    return relevant_numbers[1]