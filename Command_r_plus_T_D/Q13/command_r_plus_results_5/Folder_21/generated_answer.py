def find_second_largest_num(numbers: list[int]) -> int:
    if not numbers:
        return None
    relevant_numbers = numbers[639:976]
    relevant_numbers.sort()
    second_largest = None
    if len(relevant_numbers) > 1:
        second_largest = relevant_numbers[-2]
    return second_largest