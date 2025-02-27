def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    else:
        new_numbers = numbers[41:69]
        unique_numbers = set(new_numbers)
        if len(unique_numbers) < 2:
            return None
        else:
            sorted_numbers = sorted(unique_numbers)
            return sorted_numbers[-2]