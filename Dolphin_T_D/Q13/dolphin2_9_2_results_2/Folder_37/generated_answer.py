def find_second_largest_num(numbers):
    if 1 <= len(numbers) <= 5:
        numbers = sorted(numbers)
        if len(numbers) >= 2:
            return numbers[-2]
    return None