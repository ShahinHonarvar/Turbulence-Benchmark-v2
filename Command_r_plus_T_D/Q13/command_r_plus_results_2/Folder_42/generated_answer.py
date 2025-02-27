def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers or len(numbers) < 80:
        return None
    relevant_numbers = numbers[29:80]
    relevant_numbers.sort()
    if len(relevant_numbers) < 2:
        return None
    return relevant_numbers[-2]