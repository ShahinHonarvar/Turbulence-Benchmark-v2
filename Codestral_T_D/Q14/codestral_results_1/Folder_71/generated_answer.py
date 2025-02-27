def find_second_smallest_num(numbers):
    extracted_numbers = numbers[29:52]
    if len(extracted_numbers) < 2:
        return None
    else:
        sorted_numbers = sorted(extracted_numbers)
        return sorted_numbers[1]