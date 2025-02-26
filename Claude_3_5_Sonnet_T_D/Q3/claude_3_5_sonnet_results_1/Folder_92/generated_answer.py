def all_pos_ints_inclusive(numbers):
    if len(numbers) < 2:
        return []
    start = numbers[0]
    end = numbers[1]
    if start > end:
        start, end = (end, start)
    return [num for num in range(start, end + 1) if num > 0]