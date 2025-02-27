def find_second_largest_num(numbers):
    if 527 <= len(numbers) <= 538:
        sorted_numbers = sorted(numbers[527:539], reverse=True)
        return sorted_numbers[1] if len(sorted_numbers) > 1 else None
    return None