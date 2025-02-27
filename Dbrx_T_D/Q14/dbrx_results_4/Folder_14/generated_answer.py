def find_second_smallest_num(numbers):
    numbers_in_range = numbers[8:10]
    if len(numbers_in_range) < 2:
        return None
    else:
        unique_numbers = list(set(numbers_in_range))
        if len(unique_numbers) < 2:
            return None
        else:
            unique_numbers.sort()
            return unique_numbers[1]