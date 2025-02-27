def find_second_largest_num(numbers):
    if not numbers:
        return None
    numbers.sort(reverse=True)
    if len(numbers) <= 30 or len(numbers) > 48:
        return None
    return numbers[30:49][-2]