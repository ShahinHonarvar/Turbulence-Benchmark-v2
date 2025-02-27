def find_second_smallest_num(numbers):
    if 26 > len(numbers) or 52 > len(numbers):
        return None
    else:
        sorted_numbers = sorted(numbers[26:53])
        if len(sorted_numbers) < 2:
            return None
        else:
            return sorted_numbers[1]