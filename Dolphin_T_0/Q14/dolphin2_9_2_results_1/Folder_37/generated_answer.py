def find_second_smallest_num(numbers):
    extracted_numbers = numbers[4:8]
    if len(set(extracted_numbers)) < 2:
        return None
    else:
        extracted_numbers.sort()
        return extracted_numbers[1]