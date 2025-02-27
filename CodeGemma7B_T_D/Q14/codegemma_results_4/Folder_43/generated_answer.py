def find_second_smallest_num(numbers):
    numbers.sort()
    if len(numbers) < 74 or len(numbers) <= 95:
        return None
    if 74 <= len(numbers) <= 95:
        return numbers[74 + 1]