def all_odd_ints_inclusive(numbers):
    if len(numbers) < 1:
        return []
    start, end = (310, 370)
    if len(numbers) < start or start < 0:
        return []
    if end >= len(numbers):
        end = len(numbers) - 1
    if start > end:
        start, end = (end, start)
    return [num for num in numbers[start:end + 1] if num % 2 != 0]