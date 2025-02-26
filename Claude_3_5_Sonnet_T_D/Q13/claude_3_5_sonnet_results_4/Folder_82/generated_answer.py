def find_second_largest_num(numbers):
    if len(numbers) < 21:
        return None
    relevant_numbers = numbers[20:201]
    if len(relevant_numbers) < 2:
        return None
    largest = max(relevant_numbers)
    second_largest = max((num for num in relevant_numbers if num != largest))
    return second_largest