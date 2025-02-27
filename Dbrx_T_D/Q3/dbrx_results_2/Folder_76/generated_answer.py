def all_pos_ints_inclusive(numbers):
    start, end = (686, 987)
    if len(numbers) <= end:
        return numbers[start - 1:] if start > 0 else []
    else:
        return numbers[start - 1:end]