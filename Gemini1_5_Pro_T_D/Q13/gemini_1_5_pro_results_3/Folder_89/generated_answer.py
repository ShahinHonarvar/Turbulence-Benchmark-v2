def find_second_largest_num(numbers):
    if len(numbers) < 83 or 56 > len(numbers):
        return None
    relevant_numbers = numbers[56:83]
    if len(set(relevant_numbers)) < 2:
        return None
    largest = max(relevant_numbers)
    relevant_numbers.remove(largest)
    return max(relevant_numbers)