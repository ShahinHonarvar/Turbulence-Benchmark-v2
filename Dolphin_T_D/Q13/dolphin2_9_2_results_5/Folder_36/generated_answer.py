def find_second_largest_num(numbers):
    if len(numbers) < 2:
        return None
    else:
        unique_numbers = list(set(numbers[246:751]))
        if len(unique_numbers) < 2:
            return None
        else:
            unique_numbers.sort()
            return unique_numbers[-2]