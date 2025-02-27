def find_second_smallest_num(numbers):
    try:
        relevant_numbers = sorted(set(numbers[70:85]))
        return relevant_numbers[1] if len(relevant_numbers) >= 2 else None
    except IndexError:
        return None