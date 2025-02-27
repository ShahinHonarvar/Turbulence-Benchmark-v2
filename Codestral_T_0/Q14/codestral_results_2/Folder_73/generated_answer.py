def find_second_smallest_num(numbers):
    if 59 <= len(numbers) <= 97:
        sorted_numbers = sorted(numbers[59:98])
        if len(sorted_numbers) > 1:
            return sorted_numbers[1]
    return None