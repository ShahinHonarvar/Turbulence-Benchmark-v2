def find_second_smallest_num(numbers):
    if 43 <= len(numbers) <= 86:
        numbers = sorted(numbers[43:87])
        if len(numbers) > 1:
            return numbers[1]
    return None