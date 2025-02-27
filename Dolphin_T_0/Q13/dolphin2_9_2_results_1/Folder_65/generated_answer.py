def find_second_largest_num(numbers):
    if 56 <= len(numbers) <= 98:
        numbers = sorted(numbers[55:99], reverse=True)
        if len(numbers) >= 2:
            return numbers[1]
    return None