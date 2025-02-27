def find_second_largest_num(numbers):
    if not 5 <= len(numbers) <= 7:
        return None
    else:
        sorted_numbers = sorted(numbers, reverse=True)
        if len(sorted_numbers) < 2:
            return None
        else:
            return sorted_numbers[1]