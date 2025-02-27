def find_second_smallest_num(numbers):
    if 62 <= len(numbers) <= 78:
        sorted_numbers = sorted(numbers[62:79])
        if len(sorted_numbers) > 1:
            return sorted_numbers[1]
    return None