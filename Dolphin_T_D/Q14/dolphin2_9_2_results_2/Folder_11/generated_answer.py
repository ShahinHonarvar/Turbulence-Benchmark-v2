def find_second_smallest_num(numbers):
    if 66 <= len(numbers) <= 93:
        numbers = numbers[66:94]
        if len(set(numbers)) < 2:
            return None
        sorted_numbers = sorted(set(numbers))
        return sorted_numbers[1]
    else:
        return None