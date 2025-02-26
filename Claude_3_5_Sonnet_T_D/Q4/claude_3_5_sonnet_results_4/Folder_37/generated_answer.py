def all_pos_ints_exclusive(numbers):
    if len(numbers) < 3:
        return []
    start = numbers[1] + 1
    end = numbers[2]
    return [num for num in range(start, end) if num > 0]