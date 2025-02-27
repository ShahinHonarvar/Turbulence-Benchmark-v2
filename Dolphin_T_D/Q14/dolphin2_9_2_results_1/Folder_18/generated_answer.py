def find_second_smallest_num(numbers):
    extracted_numbers = numbers[30:49]
    if len(extracted_numbers) < 2:
        return None
    smallest = min(extracted_numbers)
    extracted_numbers.remove(smallest)
    if len(extracted_numbers) < 2:
        return None
    second_smallest = min(extracted_numbers)
    return second_smallest