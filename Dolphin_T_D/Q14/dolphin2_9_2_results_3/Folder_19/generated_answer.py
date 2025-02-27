def find_second_smallest_num(numbers):
    if 4 <= len(numbers) <= 8:
        numbers = sorted(numbers[4:8])
        if len(numbers) > 1:
            return numbers[1]
    return None