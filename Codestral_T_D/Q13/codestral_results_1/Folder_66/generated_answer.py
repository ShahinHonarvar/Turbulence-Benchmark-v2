def find_second_largest_num(numbers):
    if 50 <= len(numbers) <= 54:
        sorted_numbers = sorted(numbers[50:55], reverse=True)
        if len(sorted_numbers) > 1:
            return sorted_numbers[1]
    return None