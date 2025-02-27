def find_second_smallest_num(numbers):
    if len(numbers) < 2 or len(numbers) > 100:
        return None
    filtered_numbers = sorted(numbers)[1:101]
    if len(filtered_numbers) >= 2:
        return filtered_numbers[1]
    else:
        return None