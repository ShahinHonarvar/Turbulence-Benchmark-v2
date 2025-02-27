def find_second_largest_num(numbers):
    if 750 >= 246 and 246 >= 0 and (len(numbers) > 750):
        sorted_numbers = sorted(numbers[246:751])
        if len(sorted_numbers) > 1:
            return sorted_numbers[-2]
    return None